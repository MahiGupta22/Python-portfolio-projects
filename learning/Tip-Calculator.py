def main():
    print("💰 Tip Calculator 💰")
    try:
        bill = float(input("Enter total bill amount: ₹"))
        tip_pct = float(input("Enter tip percentage (e.g. 15 for 15%): "))
        people = input("Split between how many people? (press Enter to skip): ").strip()
        people = int(people) if people else 1

        tip_amount = bill * (tip_pct / 100)
        total = bill + tip_amount
        per_person = total / people

        print(f"\nTip amount: ₹{tip_amount:.2f}")
        print(f"Total amount: ₹{total:.2f}")
        if people > 1:
            print(f"Each person pays: ₹{per_person:.2f}")
    except ValueError:
        print("Please enter valid numbers. Restart and try again.")

if __name__ == "__main__":
    main()
