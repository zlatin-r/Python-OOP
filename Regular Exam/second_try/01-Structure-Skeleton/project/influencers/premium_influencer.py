from project.influencers.base_influencer import BaseInfluencer


class PremiumInfluencer(BaseInfluencer):
    PAYMENT_PERCENTAGE = 0.85

    def calculate_payment(self, campaign):
        return campaign.BUDGET * self.PAYMENT_PERCENTAGE

    def reached_followers(self, campaign_type: str):
        if campaign_type == 'HighBudgetCampaign':
            return (self.followers * self.engagement_rate) * 1.5

        elif campaign_type == 'LowBudgetCampaign':
            return (self.followers * self.engagement_rate) * 0.8
