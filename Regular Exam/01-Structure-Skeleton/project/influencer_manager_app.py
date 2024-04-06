from typing import List
from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    VALID_INFLUENCER_TYPES = {"PremiumInfluencer": PremiumInfluencer, "StandardInfluencer": StandardInfluencer}
    VALID_CAMPAIGN_TYPES = {"HighBudgetCampaign": HighBudgetCampaign, "LowBudgetCampaign": LowBudgetCampaign}

    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.VALID_INFLUENCER_TYPES:
            return f"{influencer_type} is not an allowed influencer type."

        influencer = next(filter(lambda inf: inf.username == username, self.influencers), None)
        if influencer:
            return f"{username} is already registered."

        new_influencer = self.VALID_INFLUENCER_TYPES[influencer_type](username, followers, engagement_rate)
        self.influencers.append(new_influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.VALID_CAMPAIGN_TYPES:
            return f"{campaign_type} is not a valid campaign type."

        campaign = next(filter(lambda c: c.campaign_id == campaign_id, self.campaigns), None)
        if campaign:
            return f"Campaign ID {campaign_id} has already been created."

        new_campaign = self.VALID_CAMPAIGN_TYPES[campaign_type](campaign_id, brand, required_engagement)
        self.campaigns.append(new_campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        try:
            influencer = next(filter(lambda inf: inf.username == influencer_username, self.influencers))
        except StopIteration:
            return f"Influencer '{influencer_username}' not found."

        try:
            campaign = next(filter(lambda c: c.campaign_id == campaign_id, self.campaigns))
        except StopIteration:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        influencer_payment = influencer.calculate_payment(campaign)
        if influencer_payment > 0.0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= influencer_payment
            influencer.campaigns_participated.append(campaign)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        result = {}

        for campaign in self.campaigns:
            if campaign.approved_influencers:
                result[campaign.CAMPAIGN_IDS] = 0
                for inf in campaign.approved_influencers:
                    for camp in inf.campaigns_participated:
                        result[campaign.CAMPAIGN_IDS] += inf.reached_followers(camp.__class__.__name__)

        return result

    def influencer_campaign_report(self, username: str):
        infl = next(filter(lambda inf: inf.username == username, self.influencers))

        if not infl.campaigns_participated:
            return f"{username} has not participated in any campaigns."

        return infl.display_campaigns_participated()

    def campaign_statistics(self):
        sorted_camps = sorted(self.campaigns, key=lambda c: (len(c.approved_influencers), -c.budget))

        result = ["$$ Campaign Statistics $$"]

        for campaign in sorted_camps:
            total_reached_followers = 0
            for inf in campaign.approved_influencers:
                total_reached_followers += inf.reached_followers(campaign.__class__.__name__)

            result.append(f"  * Brand: {campaign.brand}, "
                          f"Total influencers: {len(campaign.approved_influencers)}, "
                          f"Total budget: ${campaign.budget:.2f}, "
                          f"Total reached followers: {int(total_reached_followers)}")

        return "\n".join(result)
