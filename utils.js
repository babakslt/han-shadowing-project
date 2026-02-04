// Shared helpers for web players
// Keep in sync with Python category normalization in main.py
window.toSafeCategory = function toSafeCategory(categoryName) {
  return String(categoryName || "default")
    .replace(/[^a-zA-Z0-9 _-]/g, "")
    .trim()
    .replace(/ /g, "_");
};
