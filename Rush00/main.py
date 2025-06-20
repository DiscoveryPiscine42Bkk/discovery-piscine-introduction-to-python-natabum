tasks = []
def show_menu():
    print("\n====== Smart Farm Task Organizer ======")
    print("1. เพิ่มงานในฟาร์ม")
    print("2. แสดงรายการงานทั้งหมด")
    print("3. ลบงาน")
    print("4. สรุปจำนวนนงานในแต่ละประเภท")
    print("5. ออกจากโปรแกรม")

def add_task():
    name = input("📌 ป้อนชื่องาน: ")
    date = input("📅 ป้อนวันที่ (dd/mm/yyyy): ")
    category = input("🌾 ประเภทงาน (พืช/ปศุสัตว์/อื่นๆ): ")
    task = {"name": name, "category": category, "date": date}
    tasks.append(task)
    print("✅ เพิ่มงานสำเร็จ")

def show_tasks():
    print("\n📋 รายการงานทั้งหมด")
    if not tasks:
        print("❌ ยังไม่มีงานในรายการ")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['date']} - {task['name']} ({task['category']})")

def delete_task():
    print("\n📋 รายการงานทั้งหมด:")
    if not tasks:
        print("❌ ไม่มีงานให้ลบ")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['name']} ({task['category']}) - {task['date']}")
        try:
            index = int(input("🔻 ลำดับของงานที่ต้องการลบ: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"🗑 ลบงาน: {removed['name']}' แล้ว")
            else:
                print("❌ หมายเลขไม่ถูกต้อง")
        except:
            print("❌ กรุณาใส่ตัวเลขเท่านั้น")

def summarize_tasks():
    print("\n📊 สรุปจำนวนงานแต่ละประเภท")
    summary = {}
    for task in tasks:
        cat = task["category"]
        if cat in summary:
            summary[cat] += 1
        else:
            summary[cat] = 1
    if not summary:
        print("❌ ไม่มีงานในระบบ")
    else:
        for cat in summary:
            print(f"- {cat}: {summary[cat]} งาน")

def main():
    while True:
        show_menu()
        choice = input("เลือกเมนู (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            summarize_tasks()
        elif choice == "5":
            print("👋 ขอบคุณที่ใช้โปรแกรม Smart Farm!")
            break
        else:
            print("❌ กรุณาเลือกเมนูให้ถูกต้อง (1-5)")

main()