// prettier-ignore
// document.getElementById("quick-sort-button").addEventListener("click", quickSort(values, 0, values.length - 1));
document.getElementById("quick-sort-button").addEventListener("click", () =>  quickSort(values, 0, values.length - 1));

// reset canvas
// document.getElementById("reset-button").addEventListener("click", setup);
document.getElementById("reset-button").addEventListener("click", refreshPage);

function refreshPage() {
  window.location.reload();
}
