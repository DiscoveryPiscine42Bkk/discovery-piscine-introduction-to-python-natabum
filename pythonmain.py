# main.py
from typing import list, Dict

class FarmTask:
  def __init__(self, name: str, date: str,task_type: str):
    self.name = name
    self.date = date
    self.task_type = task_type

class TaskManager:
  def _init_(self):
    self.tasks: List[FarmTask] = []

  def add_task(self, name: str, date: str, task_type: str):
    """เพิ่มงานใหม่"""
    new_task = FarmTask(name, date, task_type)
    self.tasks.append(new_task)
    print("เพิ่มงานสำเร็จ")

  def show_all_tasks(self):
    """แสดงรายงานทั้งหมด"""
    if not self.tasks:
      print("ยังไม่มีงานในรายการ")
      return

    print("\nรายการงานทั้งหมด:")
    for i, task in enumerate(self.tasks, 1):
      print(f"{i}. {task.date} - {task.name} ({task.task_type})")

   def delete_task(self, task_index: int):
     """ลบงานตามลำดับที่ระบุ"""
     if 1 <= task_index <= len(self.tasks):
       removed_task = self.tasks.pop(task_indeex - 1)
       print(f"ลบงาน: {removed_task.name}c]h;")
     else:
       print("ลำดับงานไม่ถูกต้อง")

   def summerize_tasks(self):
     """สรุปจำนวนงานแต่ละประเภท"""
     if not self.tasks:
       print("ยังไม่มีงานในรายการ")
       return

       type_counts: Dict[str, int] = {}
       for task in self.tasks:
           type_counts[task.task_type] = type_counts.get(task.task_type, 0) + 1

       print("\nสรุปจำนวนงานแต่ละประเภท:")
       for task_type, count in type_counts.items():
         print(f"- {task_type}: {count} งาน")

def display_menu():
  """แสดงเมนูหลัก"""
  print("\n" + "="*40)
  print("Smart Farm Task Orgenizer")
  print("="*40)
  print("1. เพื่มงานในฟาร์ม")
  print("2. แสดงรายการงานทั้งหมด")
  print("3. ลบงาน")
  print("4. สรุปจำนวนงานในแต่ละประเภท")
  print("5. ออกจากโปรแกรม")
  print("="*40)

def main():
  manager = TaskManager()

while True:
  display_menu()
  choice = input("เลือกเมนู (1-5): ").strip()

  if choice == "1":
    name = input("ป้อนชื่องาน: ")
    date = input("ป้อนวันที่ (dd/mm/yyyy): ")
    task_type = input("ประเภทงาน (พืชผัก/ปลูกสัตว์/อื่นๆ): ")
    manager.add_task(name, data, task_type)

  elif choice == "2":
    manager.show_all_tasks()

  elif choice == "3":
    manager.show_all_tasks()
    if manager.tasks:
      try:
        task_num = int(input("ลำดับของงานที่่ต้องการจะลบ: "))
        manager.delete_task(task_num)
      except ValueError:
        print("กรุณาป้อนตัวเลขเท่านั้น")

  elif choice == "4":
       manager.summerize_tasks()

  elif choice == "5":
    print("\nขอบคุณที่ใช้โปรแกรม smart Farm!")
    break

  else:
    print("กรุณาเลือกเมนู 1-5 เท่านั้น")

if _name_ == "_main_":
  main() 