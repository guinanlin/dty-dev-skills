#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""财务分析计算器 - Z-Score破产预警 + 杜邦分解四层全链路"""

import sys
import json


def dupont_analysis(net_income: float, revenue: float, total_assets: float,
                    equity: float, cogs: float = None, sga: float = None,
                    current_assets: float = None, non_current_assets: float = None,
                    current_liab: float = None, non_current_liab: float = None) -> dict:
    net_margin = net_income / revenue if revenue else 0
    asset_turnover = revenue / total_assets if total_assets else 0
    equity_multiplier = total_assets / equity if equity else 0
    roe = net_margin * asset_turnover * equity_multiplier
    roa = net_income / total_assets if total_assets else 0
    result = {"ROE": round(roe, 4), "ROA": round(roa, 4),
              "净利率": round(net_margin, 4), "总资产周转率": round(asset_turnover, 4),
              "权益乘数": round(equity_multiplier, 4),
              "资产负债率": round(1 - 1 / equity_multiplier, 4) if equity_multiplier else 0}
    if sga is not None and cogs is not None:
        result["费用率"] = round(sga / revenue, 4) if revenue else 0
        result["毛利率"] = round((revenue - cogs) / revenue, 4) if revenue else 0
    if current_assets is not None:
        result["流动资产占比"] = round(current_assets / total_assets, 4) if total_assets else 0
    if current_liab is not None:
        result["流动比率"] = round(current_assets / current_liab, 4) if current_liab else 0
    return result


def zscore_mfg(working_capital: float, retained_earnings: float, ebit: float,
               market_cap: float, total_liabilities: float, revenue: float,
               total_assets: float) -> dict:
    x1 = working_capital / total_assets
    x2 = retained_earnings / total_assets
    x3 = ebit / total_assets
    x4 = market_cap / total_liabilities if total_liabilities else 0
    x5 = revenue / total_assets
    z = 1.2 * x1 + 1.4 * x2 + 3.3 * x3 + 0.6 * x4 + 1.0 * x5
    if z > 2.99:
        zone = "安全区"
    elif z > 1.81:
        zone = "灰色区"
    else:
        zone = "危险区"
    return {"Z值": round(z, 4), "区间": zone,
            "X1_营运资本/总资产": round(x1, 4), "X2_留存收益/总资产": round(x2, 4),
            "X3_EBIT/总资产": round(x3, 4), "X4_市值/负债": round(x4, 4),
            "X5_营收/总资产": round(x5, 4)}


def zscore_non_mfg(working_capital: float, retained_earnings: float,
                   ebit: float, equity_book: float, total_liabilities: float,
                   total_assets: float) -> dict:
    x1 = working_capital / total_assets
    x2 = retained_earnings / total_assets
    x3 = ebit / total_assets
    x4 = equity_book / total_liabilities if total_liabilities else 0
    z = 6.56 * x1 + 3.26 * x2 + 6.72 * x3 + 1.05 * x4
    if z > 2.6:
        zone = "安全区"
    elif z > 1.1:
        zone = "灰色区"
    else:
        zone = "危险区"
    return {"Z值": round(z, 4), "区间": zone,
            "X1_营运资本/总资产": round(x1, 4), "X2_留存收益/总资产": round(x2, 4),
            "X3_EBIT/总资产": round(x3, 4), "X4_权益/负债": round(x4, 4)}


def main():
    if len(sys.argv) < 2:
        print("用法: python financial_analyzer.py '<json>'")
        print('  操作: dupont / zscore_mfg / zscore_non_mfg')
        print('  示例: python financial_analyzer.py \'{"op":"dupont","net_income":500,')
        print('    "revenue":10000,"total_assets":8000,"equity":3000}\'')
        sys.exit(1)
    d = json.loads(sys.argv[1])
    op = d.pop("op", "dupont")
    if op == "dupont":
        print(json.dumps(dupont_analysis(**d), ensure_ascii=False, indent=2))
    elif op == "zscore_mfg":
        print(json.dumps(zscore_mfg(**d), ensure_ascii=False, indent=2))
    elif op == "zscore_non_mfg":
        print(json.dumps(zscore_non_mfg(**d), ensure_ascii=False, indent=2))
    else:
        print(f"未知操作: {op}")


if __name__ == "__main__":
    main()
