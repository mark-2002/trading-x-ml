class PriceInsightsPortfolioGeneration(QCAlgorithm):
    def Initialize(self):
        self.UniverseSettings.Resolution = Resolution.Minute
        self.SetStartDate(2013,10,7)
        self.SetEndDate()
        self.SetCash(100000)
        symbols = [Symbol.Create("SPY",SecurityType.Equity,Market.USA)]
        self.SetUniverseSelection(ManualUniverseSelectionModel(symbols))
        self.SetAlpha(ConstantAlphaModel(InsightType.Price,InsightDirection.Up,timedelta(minutes=20),0.025,0.25))
        self.SetPortfolioConstruction(AccumulativeInsightPortfolioConstructionModel())
        self.SetExecution(ImmediateExecutionModel())

        def OnEndOfAlgorithm(self):
        # holdings value should be 0.03 - to avoid price fluctuation issue we compare with 0.06 and 0.01
        if (self.Portfolio.TotalHoldingsValue > self.Portfolio.TotalPortfolioValue * 0.06
            or self.Portfolio.TotalHoldingsValue < self.Portfolio.TotalPortfolioValue * 0.01):
            raise ValueError("Unexpected Total Holdings Value: " + str(self.Portfolio.TotalHoldingsValue))
