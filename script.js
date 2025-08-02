// Wait for the DOM to fully load
document.addEventListener('DOMContentLoaded', () => {
    // Select DOM elements
    const addButton = document.getElementById('add-task-btn');
    const taskInput = document.getElementById('task-input');
    const taskList = document.getElementById('task-list');

    // Function to add a new task
    function addTask() {
        const taskText = taskInput.value.trim();

        // Prevent empty tasks
        if (taskText === '') {
            alert('Please enter a task.');
            return;
        }

        // Create a list item
        const li = document.createElement('li');
        li.textContent = taskText;

        // Create a remove button
        const removeButton = document.createElement('button');
        removeButton.textContent = 'Remove';

        // ✅ Use classList.add (as required)
        removeButton.classList.add('remove-btn');

        // Remove task on click
        removeButton.onclick = () => {
            taskList.removeChild(li);
            saveTasks(); // update localStorage
        };

        // Append the remove button to the list item
        li.appendChild(removeButton);

        // Append the list item to the task list
        taskList.appendChild(li);

        // Clear the input field
        taskInput.value = '';

        // Save to localStorage
        saveTasks();
    }

    // Save current tasks to localStorage
    function saveTasks() {
        const tasks = [];
        taskList.querySelectorAll('li').forEach(li => {
            tasks.push(li.firstChild.textContent); // Exclude the button text
        });
        localStorage.setItem('todoTasks', JSON.stringify(tasks));
    }

    // Load tasks from localStorage
    function loadTasks() {
        const savedTasks = JSON.parse(localStorage.getItem('todoTasks')) || [];
        savedTasks.forEach(taskText => {
            const li = document.createElement('li');
            li.textContent = taskText;

            const removeButton = document.createElement('button');
            removeButton.textContent = 'Remove';

            // ✅ Use classList.add here too
            removeButton.classList.add('remove-btn');

            removeButton.onclick = () => {
                taskList.removeChild(li);
                saveTasks();
            };

            li.appendChild(removeButton);
            taskList.appendChild(li);
        });
    }

    // ✅ Add task when button is clicked
    addButton.addEventListener('click', addTask);

    // ✅ Add task on pressing "Enter"
    taskInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            addTask();
        }
    });

    // ✅ Load saved tasks when page loads
    loadTasks();
});
