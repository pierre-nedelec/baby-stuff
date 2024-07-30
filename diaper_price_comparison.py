def calculate_annual_costs(
    diapers_per_day,
    diaper_info_redyper,
    diaper_info_pamper,
    months_per_stage,
    subscription_cost_redyper,
):
    total_diapers_per_stage = []
    total_cost_redyper = 0.0
    total_cost_pamper = 0.0
    cost_per_stage_redyper = []
    cost_per_stage_pamper = []

    for stage in range(len(months_per_stage)):
        days_in_stage = months_per_stage[stage] * 30  # Assuming 30 days per month
        diapers_in_stage = days_in_stage * diapers_per_day[stage]
        total_diapers_per_stage.append(diapers_in_stage)

        # REDYPER cost calculations
        redyper_price_per_diaper = (
            diaper_info_redyper[stage]["price"] / diaper_info_redyper[stage]["count"]
        )
        cost_redyper_stage = diapers_in_stage * redyper_price_per_diaper

        # Pamper cost calculations
        pamper_price_per_diaper = (
            diaper_info_pamper[stage]["price"] / diaper_info_pamper[stage]["count"]
        )
        cost_pamper_stage = diapers_in_stage * pamper_price_per_diaper

        total_cost_redyper += cost_redyper_stage
        total_cost_pamper += cost_pamper_stage
        cost_per_stage_redyper.append(int(cost_redyper_stage))
        cost_per_stage_pamper.append(int(cost_pamper_stage))

    # Adding subscription cost for REDYPER
    total_cost_redyper += subscription_cost_redyper * 12  # 12 months in a year

    return (
        total_cost_redyper,
        total_cost_pamper,
        total_diapers_per_stage,
        cost_per_stage_redyper,
        cost_per_stage_pamper,
    )


def main():
    # Updated diapers per day and prices based on latest data
    diapers_per_day = [
        10,
        9,
        7,
        5,
        4,
        4,
        3,
    ]  # Number of diapers used per day for each stage
    months_per_stage = [1, 3, 4, 16, 12, 12, 4]  # Number of months each stage lasts

    # REDYPER information: list of dicts with price and count per stage
    diaper_info_redyper = [
        {"price": 13.50, "count": 34},  # Stage 1: Newborn
        {"price": 13.50, "count": 36},  # Stage 2: Size 1
        {"price": 13.50, "count": 32},  # Stage 3: Size 2
        {"price": 13.50, "count": 28},  # Stage 4: Size 3
        {"price": 13.50, "count": 24},  # Stage 5: Size 4
        {"price": 13.50, "count": 20},  # Stage 6: Size 5
        {"price": 10.50, "count": 14},  # Stage 7: Size 6
    ]

    # Pamper information: list of dicts with price and count per stage
    diaper_info_pamper = [
        {"price": 29, "count": 84},  # Stage 1: Newborn
        {"price": 29, "count": 96},  # Stage 2: Size 1
        {"price": 29, "count": 84},  # Stage 3: Size 2
        {"price": 29, "count": 78},  # Stage 4: Size 3
        {"price": 32, "count": 66},  # Stage 5: Size 4
        {"price": 32, "count": 58},  # Stage 6: Size 5
        {"price": 29, "count": 50},  # Stage 7: Size 6
    ]

    subscription_cost_redyper = 34  # Monthly subscription cost for REDYPER

    # Calculate annual costs
    (
        annual_cost_redyper,
        annual_cost_pamper,
        total_diapers_per_stage,
        cost_per_stage_redyper,
        cost_per_stage_pamper,
    ) = calculate_annual_costs(
        diapers_per_day,
        diaper_info_redyper,
        diaper_info_pamper,
        months_per_stage,
        subscription_cost_redyper,
    )

    print(f"Annual cost for REDYPER: ${annual_cost_redyper:.2f}")
    print(f"Annual cost for Pamper: ${annual_cost_pamper:.2f}")
    print(f"Total diapers used per stage: {total_diapers_per_stage}")
    print(f"Cost per stage for REDYPER: {cost_per_stage_redyper}")
    print(f"Cost per stage for Pamper: {cost_per_stage_pamper}")


if __name__ == "__main__":
    main()
