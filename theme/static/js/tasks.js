document.addEventListener("DOMContentLoaded", function () {
  const taskForm = document.getElementById("taskCreateForm");

  if (taskForm) {
      taskForm.addEventListener("submit", function (event) {
          event.preventDefault(); // Prevent default form submission

          const form = this;
          const actionUrl = form.action;
          const formData = new FormData(form);

          fetch(actionUrl, {
              method: "POST",
              body: formData,
              headers: {
                  "X-Requested-With": "XMLHttpRequest"
              }
          })
          .then(response => response.json().catch(() => ({ success: false, error: "Invalid JSON response" })))
          .then(data => {
              if (data.success) {
                  Swal.fire({
                      title: "Success!",
                      text: "Task created successfully.",
                      icon: "success",
                      confirmButtonText: "OK"
                  }).then(() => {
                      window.location.href = "/tasks/";
                  });

                  form.reset();
              } else {
                  let errorMessage = data.error || "Something went wrong.";
                  if (typeof data.error === "object") {
                      errorMessage = Object.values(data.error).join("\n");
                  }

                  Swal.fire({
                      title: "Error!",
                      text: errorMessage,
                      icon: "error",
                      confirmButtonText: "OK"
                  });
              }
          })
          .catch(error => {
              console.error("Fetch Error:", error);
              Swal.fire({
                  title: "Error!",
                  text: "Something went wrong. Please try again.",
                  icon: "error",
                  confirmButtonText: "OK"
              });
          });
      });
  }
});

document.addEventListener("DOMContentLoaded", function () {
  const previewButtons = document.querySelectorAll("[data-modal-target='readTaskModal']");

  previewButtons.forEach(button => {
      button.addEventListener("click", function () {
          const taskTitle = this.getAttribute("data-title");
          const taskDescription = this.getAttribute("data-description");
          const taskStatus = this.getAttribute("data-status");
          const taskProject = this.getAttribute("data-project");

          document.getElementById("modalTaskTitle").textContent = taskTitle;
          document.getElementById("modalTaskDescription").textContent = taskDescription;
          document.getElementById("modalTaskStatus").textContent = taskStatus;
          document.getElementById("modalTaskProject").textContent = taskProject;
      });
  });
});
