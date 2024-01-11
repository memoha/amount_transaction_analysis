import pandas as pd

def calc_avg_trans_amt(trans_amt):
    monthly_totals = {}
    monthly_counts = {}

    for date, amount in trans_amt:
        date_str = str(date)
        month_key = date_str[:7]

        monthly_totals[month_key] = monthly_totals.get(month_key, 0) + amount
        monthly_counts[month_key] = monthly_counts.get(month_key, 0) + 1

        avg_trans_amt = {}
        for month, total in monthly_totals.items():
            avg_trans_amt[month] = total/monthly_counts[month]

    return avg_trans_amt


excel_file_path = r"C:\Users\Megha\OneDrive\Documents\intropython\intropython\avg_trans_amt.xlsx"
df = pd.read_excel(r"C:\Users\Megha\OneDrive\Documents\intropython\intropython\avg_trans_amt.xlsx")

trans_amt = df[[ "Date", "Amount"]].values.tolist()

result = calc_avg_trans_amt(trans_amt)
print(result)