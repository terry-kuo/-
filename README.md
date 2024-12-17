    # 連接功能
    self.addButton.clicked.connect(self.add_task)
    self.deleteButton.clicked.connect(self.delete_task)
    self.markCompleteButton.clicked.connect(self.mark_complete)

def add_task(self):
    task = self.taskInput.text()
    if task.strip():
        self.taskList.addItem(task)
        self.taskInput.clear()
    else:
        QMessageBox.warning(self, "Error", "Task cannot be empty")

def delete_task(self):
    selected_task = self.taskList.currentItem()
    if selected_task:
        self.taskList.takeItem(self.taskList.row(selected_task))
    else:
        QMessageBox.warning(self, "Error", "No task selected")

def mark_complete(self):
    selected_task = self.taskList.currentItem()
    if selected_task:
        selected_task.setText(f"{selected_task.text()} (Completed)")
    else:
        QMessageBox.warning(self, "Error", "No task selected")
