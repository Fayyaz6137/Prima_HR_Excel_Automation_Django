import pandas as pd
from datetime import datetime
from openpyxl import load_workbook


def process_csv(file_path):
    # ==============================
    # 1. Read Excel file data
    # ==============================
    assumptions = pd.read_excel(file_path, sheet_name="input_assumptions")
    input_data = pd.read_excel(file_path, sheet_name="input_data")
    lookup = pd.read_excel(file_path, sheet_name="lookup_probability")

    # ==============================
    # 2. Extract assumptions
    # ==============================
    valuation_date = pd.to_datetime(
        assumptions.loc[assumptions.iloc[:, 0] == "valuation_date"].iloc[0, 1]
    )
    # valuation_date

    discount_rate = float(
        str(assumptions.loc[assumptions.iloc[:, 0] == "discount_rate"].iloc[0, 1]).replace("%", "")
    )
    # discount_rate
    salary_increase_rate = float(
        str(assumptions.loc[assumptions.iloc[:, 0] == "salary_increase_rate"].iloc[0, 1]).replace("%", "")
    )
    # salary_increase_rate
    retirement_age = int(
        assumptions.loc[assumptions.iloc[:, 0] == "retirement_age"].iloc[0, 1]
    )
    # retirement_age

    # ==============================
    # 3. Select Employee 1
    # ==============================
    input_data.dropna()
    input_data = input_data[1:]  # keep rows from index 1 onward
    input_data.columns = input_data.iloc[0]  # set the header row
    input_data = input_data[1:]  # drop the old header row
    input_data = input_data.reset_index(drop=True)
    # input_data

    emp = input_data[input_data["emp_id"] == 1].iloc[0]
    dob = pd.to_datetime(emp["date_birth"])
    current_salary = emp["salary"]
    #emp

    # ==============================
    # 4. Current age
    # ==============================
    current_age = int((valuation_date - dob).days / 365.25)

    # ==============================
    # 5. Prepare probability table
    # ==============================
    lookup["qx"] = lookup["qx"].astype(str).str.replace("%", "").astype(float) * 100
    lookup["px"] = lookup["px"].astype(str).str.replace("%", "").astype(float) * 100

    # ==============================
    # 6. Build calculation table
    # ==============================
    rows = []

    for age in range(current_age, retirement_age):
        years_ahead = age - current_age

        future_salary = current_salary * ((1 + salary_increase_rate) ** years_ahead)

        prob_row = lookup[lookup["age"] == age].iloc[0]
        qx = prob_row["qx"]
        px = prob_row["px"]

        expected_death_outflow = (future_salary * qx) / 100

        rows.append({
            "Age": age,
            "Future Salary": round(future_salary, 2),
            "Survival Probability": round(px, 3),
            "Death Probability": round(qx, 3),
            "Expected Death Outflow": round(expected_death_outflow, 2)
        })

    calculation_df = pd.DataFrame(rows)
    # calculation_df

    # ==============================
    # 7. Write back to Excel (new sheet)
    # ==============================
    with pd.ExcelWriter(file_path, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
        calculation_df.to_excel(writer, sheet_name="calculation", index=False)

    print("Calculation sheet created successfully!")

    # df = pd.read_csv(input_path)
    # # df['Total'] = df['Quantity'] * df['Price']
    # df.to_csv(output_path, index=False)

