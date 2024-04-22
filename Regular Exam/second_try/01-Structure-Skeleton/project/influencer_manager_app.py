from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    VALID_INFLUENCER_TYPES = {"PremiumInfluencer": PremiumInfluencer, "StandardInfluencer": StandardInfluencer}
    VALID_CAMPAIGNS_TYPES = {"HighBudgetCampaign": HighBudgetCampaign, "LowBudgetCampaign":LowBudgetCampaign}

    def __init__(self):
        self.influencers = []
        self.campaigns = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.VALID_INFLUENCER_TYPES:
            return f"{influencer_type} is not an allowed influencer type."

        try:
            next(filter(lambda inf: inf.username == username, self.influencers))
            return f"{username} is already registered."
            # TODO CHECK THIS IF IS OK
        except StopIteration:
            self.influencers.append(self.VALID_INFLUENCER_TYPES[influencer_type](username, followers, engagement_rate))
            return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.VALID_CAMPAIGNS_TYPES:
            return f"{campaign_type} is not a valid campaign type."

        try:
            next(filter(lambda camp: campaign_id == camp.campaign_id, self.campaigns))
            return f"Campaign ID {campaign_id} has already been created."
            # TODO CHECK HERE IF IS OK
        except StopIteration:
            self.campaigns.append(self.VALID_CAMPAIGNS_TYPES[campaign_type](campaign_id, brand, required_engagement))
            return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

