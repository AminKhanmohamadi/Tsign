$(document).ready(function () {

    $('.view-file').on('click', function () {
        const name = $(this).data('name');
        const type = $(this).data('type');
        const size = $(this).data('size');
        const date = $(this).data('date');
        const url = $(this).data('url');

        $('#fileName').text(name);
        $('#fileType').text(type);
        $('#fileSize').text(size);
        $('#fileDate').text(date);

        if (type === 'image') {
            $('#filePreview').html(`<img src="${url}" class="img-fluid" alt="${name}">`);
        } else if (type === 'video') {
            $('#filePreview').html(`
                <video class="w-100" controls>
                    <source src="${url}" type="video/mp4">
                        Your browser does not support video playback.
                </video>`);
        } else {
            $('#filePreview').html('<p>Preview is not supported for this file type.</p>');
        }
    });

    $('.delete-file').on('click', function () {
        const fileId = $(this).data('id');
        $('#file_id').val(fileId);

        const deleteModal = new bootstrap.Modal($('#deleteFileModal')[0]);
        deleteModal.show();
    });
    $('#deleteFileForm').on('submit', function (event) {
        event.preventDefault();

        const fileId = $('#file_id').val();
        const deleteUrl = $('.delete-file[data-id="' + fileId + '"]').data('url');

        $.ajax({
            url: deleteUrl,
            method: 'POST',
            data: {
                'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
            },
            success: function (data) {
                if (data.success) {
                    const deleteModal = bootstrap.Modal.getInstance($('#deleteFileModal')[0]);
                    deleteModal.hide();
                    $('[data-id="' + fileId + '"]').closest('.file-row').remove();
                } else {
                    console.error("Error deleting file:", data.message);
                }
            },
            error: function (error) {
                console.error("Error:", error);
            }
        });
    });

    $('.delete-folder').on('click', function () {
        const folderId = $(this).data('id');
        $('#folder_id').val(folderId);

        const deleteModal = new bootstrap.Modal($('#deleteFolderModal')[0]);
        deleteModal.show();
    });
    $('#deleteFolderForm').on('submit', function (event) {
        event.preventDefault();

        const folderId = $('#folder_id').val();
        const deleteUrl = $('.delete-folder[data-id="' + folderId + '"]').data('url');
        const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

        $.ajax({
            url: deleteUrl,
            method: 'POST',
            contentType: 'application/json',
            headers: {
                'X-CSRFToken': csrfToken
            },
            data: JSON.stringify({
                'folder_id': folderId
            }),
            success: function (data) {
                if (data.success) {
                    const deleteModal = bootstrap.Modal.getInstance($('#deleteFolderModal')[0]);
                    deleteModal.hide();
                    $('[data-id="' + folderId + '"]').closest('.folder-row').remove();
                } else {
                    console.error("Error deleting folder:", data.message);
                }
            },
            error: function (error) {
                console.error("Error:", error);
            }
        });
    });

});
