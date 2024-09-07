// 페이지에서 텍스트가 선택되었을 때 이벤트 리스너 추가
document.addEventListener('mouseup', function () {
    const selectedText = window.getSelection().toString().trim();  // 선택한 텍스트 추출

    if (selectedText.length > 0) {
        // 선택한 텍스트를 서버로 전달해보자고
        fetch('http://127.0.0.1:8000/api/predict/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                selected_text: selectedText
            })
        })
            .then(response => response.json())
            .then(data => {
                // 서버 응답을 로컬 저장소에 저장{}
                chrome.storage.local.set({ serverResponse: data.message }, function () {
                    if (chrome.runtime.lastError) {
                        console.error('Error saving to local storage:', chrome.runtime.lastError);
                    } else {
                        console.log('Data saved successfully!');
                    }


                });
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }
});
