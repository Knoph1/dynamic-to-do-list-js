document.addEventListener('DOMContentLoaded', () => {
    const addButton = document.getElementById('add-task-btn');
    const taskInput = document.getElementById('task-input');
    const taskList = document.getElementById('task-list');

    // Load and display tasks on page load
    loadTasks();

    // Event: Add task on button click
    addButton.addEventListener('click', () => {
        const taskText = taskInput.value.trim();
        if (taskText !== '') {
            addTask(taskText, true); // true = save to localStorage
            taskInput.value = ''; // clear input
        } else {
            alert('Please enter a task.');
        }
    });

    // Event: Add task on pressing "Enter"
    taskInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            const taskText = taskInput.value.trim();
            if (taskText !== '') {
                addTask(taskText, true);
                taskInput.value = '';
            } else {
                alert('Please enter a task.');
            }
        }
    });

    // Function to add task to the DOM and optionally save
    function addTask(taskText, save = true) {
        const li = document.createElement('li');
        li.textContent = taskText;

        const removeButton = document.createElement('button');
        removeButton.textContent = 'Remove';
        removeButton.classList.add('remove-btn');

        removeButton.onclick = () => {
            taskList.removeChild(li);
            removeFromLocalStorage(taskText);
        };

        li.appendChild(removeButton);
        taskList.appendChild(li);

        if (save) {
            saveToLocalStorage(taskText);
        }
    }

    // Save a task to localStorage
    function saveToLocalStorage(taskText) {
        const tasks = JSON.parse(localStorage.getItem('tasks') || '[]');
        tasks.push(taskText);
        localStorage.setItem('tasks', JSON.stringify(tasks));
    }

    // Remove a task from localStorage
    function removeFromLocalStorage(taskText) {
        const tasks = JSON.parse(localStorage.getItem('tasks') || '[]');
        const updatedTasks = tasks.filter(task => task !== taskText);
        localStorage.setItem('tasks', JSON.stringify(updatedTasks));
    }

    // Load all tasks from localStorage
    function loadTasks() {
        const storedTasks = JSON.parse(localStorage.getItem('tasks') || '[]');
        storedTasks.forEach(taskText => addTask(taskText, false)); // false = don't save again
    }
});
