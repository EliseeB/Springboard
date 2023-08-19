$('.table').on('click', '.delete-btn', function() {
    $(this).closest('tr').remove(); // Use closest() to find the nearest parent <tr> and remove it
});
