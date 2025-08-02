document.addEventListener("DOMContentLoaded", function () {
  const taskInput = document.getElementById("task-input");
  const addButton = document.getElementById("add-button");
  const taskList = document.getElementById("task-list");

  // Function to add a new task
  function addTask() {
    const taskText = taskInput.value.trim();

    if (taskText !== "") {
      // Create <li> element
      const li = document.createElement("li");

      // Create span to hold task text (for better separation)
      const taskSpan = document.createElement("span");
      taskSpan.textContent = taskText;

      // Create "Remove" button
      const removeButton = document.createElement("button");
      removeButton.textContent = "Remove";
      removeButton.classList.add("remove-btn");

      // Add event listener to remove the task when button is clicked
      removeButton.addEventListener("click", function () {
        taskList.removeChild(li);
      });

      // Append text and button to li, then li to task list
      li.appendChild(taskSpan);
      li.appendChild(removeButton);
      taskList.appendChild(li);

      // Clear input field
      taskInput.value = "";
    }
  }

  // Event listener for "Add" button click
  addButton.addEventListener("click", addTask);

  // Event listener for Enter key in input field
  taskInput.addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
      addTask();
    }
  });
});
