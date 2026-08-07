class AffordabilityEngine:

    def evaluate(
        self,
        metrics: AffordabilityMetrics
    ) -> AffordabilityResult:

        eligible = self._determine_eligibility(metrics)

        reason = self._determine_reason(
            metrics,
            eligible
        )

        return AffordabilityResult(
            eligible=eligible,
            reason=reason
        )