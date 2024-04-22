from project.campaigns.base_campaign import BaseCampaign


class LowBudgetCampaign(BaseCampaign):
    BUDGET = 2_500

    def check_eligibility(self, engagement_rate: float):
        return engagement_rate >= self.required_engagement * 0.9
