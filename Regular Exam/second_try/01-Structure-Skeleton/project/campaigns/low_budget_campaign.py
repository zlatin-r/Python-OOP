from project.campaigns.base_campaign import BaseCampaign


class LowBudgetCampaign(BaseCampaign):

    def __init__(self, campaign_id, brand, required_engagement):
        super().__init__(campaign_id, brand, 2500, required_engagement)

    def check_eligibility(self, engagement_rate: float):
        return engagement_rate >= self.required_engagement * 0.9
