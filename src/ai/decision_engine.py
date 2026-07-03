class DecisionEngine:

    def decide(
        self,
        bias,
        liquidity_sweep,
        mss,
        fvg=False,
        order_block=False,
        killzone=False,
    ):

        score = 0
        reasons = []

        # HTF Bias
        if bias == "BULLISH":
            score += 20
            reasons.append("HTF Bullish")
        elif bias == "BEARISH":
            score += 20
            reasons.append("HTF Bearish")

        # Liquidity Sweep
        if liquidity_sweep:
            score += 20
            reasons.append("Liquidity Sweep")

        # MSS
        if isinstance(mss, dict) and mss.get("direction") != "NONE":
            score += 20
            reasons.append("Market Structure Shift")

        # FVG
        if fvg:
            score += 20
            reasons.append("Fair Value Gap")

        # Order Block
        if order_block:
            score += 10
            reasons.append("Order Block")

        # Kill Zone
        if killzone:
            score += 10
            reasons.append("Kill Zone")

        if score >= 80:
            decision = "STRONG BUY / SELL"

        elif score >= 60:
            decision = "BUY / SELL"

        else:
            decision = "NO TRADE"

        return {
            "score": score,
            "decision": decision,
            "reasons": reasons,
        }