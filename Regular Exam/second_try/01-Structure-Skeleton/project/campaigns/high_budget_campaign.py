from project.campaigns.base_campaign import BaseCampaign


class HighBudgetCampaign(BaseCampaign):
    BUDGET = 5_000

    def check_eligibility(self, engagement_rate: float):
        return engagement_rate >= self.required_engagement * 1.2
