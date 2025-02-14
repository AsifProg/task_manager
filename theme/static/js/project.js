
document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("projectCreateForm").addEventListener("submit", function (event) {
      event.preventDefault();

      const form = this;
      const actionUrl = form.action;
      const formData = new FormData(form);

      fetch(actionUrl, {
          method: "POST",
          body: formData
      })
      .then(response => response.json())
      .then(data => {
          if (data.success) {
              document.getElementById("createProjectModal").classList.add("hidden");

              Swal.fire({
                  title: "Success!",
                  text: "Project created successfully.",
                  icon: "success",
                  confirmButtonText: "OK"
              }).then(() => {
                  location.reload();
              });

              form.reset();
          } else {
              Swal.fire({
                  title: "Error!",
                  text: data.error || "Something went wrong.",
                  icon: "error",
                  confirmButtonText: "OK"
              });
          }
      })
      .catch(error => {
          console.error("Error:", error);
          Swal.fire({
              title: "Error!",
              text: "Something went wrong.",
              icon: "error",
              confirmButtonText: "OK"
          });
      });
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const previewButtons = document.querySelectorAll("[data-modal-target='readProjectModal']");

  previewButtons.forEach(button => {
      button.addEventListener("click", function () {
          const projectName = this.getAttribute("data-name");
          const projectDescription = this.getAttribute("data-description");

          document.getElementById("modalProjectName").textContent = projectName;
          document.getElementById("modalProjectDescription").textContent = projectDescription;
      });
  });
});


document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("[data-modal-toggle='deleteModal']").forEach(button => {
      button.addEventListener("click", function () {
          const projectId = this.getAttribute("data-id");
          document.getElementById("deleteProjectId").value = projectId;
          document.getElementById("projectDeleteForm").action = `/tasks/projects/${projectId}/delete/`;
      });
  });

  document.getElementById("projectDeleteForm").addEventListener("submit", function (event) {
      event.preventDefault();

      const form = this;
      const projectId = document.getElementById("deleteProjectId").value;
      const actionUrl = form.action;

      fetch(actionUrl, {
          method: "POST",
          headers: {
              "X-CSRFToken": form.querySelector("[name=csrfmiddlewaretoken]").value,
              "Content-Type": "application/json",
          },
          body: JSON.stringify({})
      })
      .then(response => response.json())
      .then(data => {
          if (data.success) {
              document.getElementById("deleteModal").classList.add("hidden");

              Swal.fire({
                  title: "Deleted!",
                  text: "The project has been deleted successfully.",
                  icon: "success",
                  confirmButtonText: "OK"
              }).then(() => {
                location.reload();
            });
          } else {
              Swal.fire({
                  title: "Error!",
                  text: "Something went wrong while deleting.",
                  icon: "error",
                  confirmButtonText: "OK"
              });
          }
      })
      .catch(error => {
          console.error("Error:", error);
          Swal.fire({
              title: "Error!",
              text: "Something went wrong.",
              icon: "error",
              confirmButtonText: "OK"
          });
      });
  });
});


