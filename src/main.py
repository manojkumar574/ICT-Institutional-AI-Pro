from core.analyzer import Analyzer

print("=" * 50)
print("ICT Institutional AI Pro v1")
print("=" * 50)

analyzer = Analyzer()

result = analyzer.analyze("BTCUSDT")

for key, value in result.items():
    print(f"{key}: {value}")