// 로컬 스토리지에서 서버의 응답을 불러와 팝업창에 표시
//chrome.storage.local.get(['serverResponse'], function (result) {
//    const responseElement = document.getElementById('serverResponse');
//
//    if (result.serverResponse) {
//        responseElement.textContent = result.serverResponse;  // 서버 응답 표시
//    } else {
//       responseElement.textContent = 'No response yet.';
//    }
//});


document.addEventListener('DOMContentLoaded', function () {
    // 로컬 스토리지에서 서버 응답을 불러와 팝업창에 표시
    chrome.storage.local.get(['serverResponse'], function (result) {
        const responseElement = document.getElementById('serverResponse');

        // 로컬 저장소에서 서버 응답을 가져왔는지 확인
        if (chrome.runtime.lastError) {
            //console.error('Error retrieving data:', chrome.runtime.lastError);
            responseElement.textContent = 'Error retrieving data';
        } else {
            //console.log('Retrieved data from local storage:', result.serverResponse);

            if (result.serverResponse) {
                responseElement.textContent = result.serverResponse;  // 서버 응답 표시
            } else {
                responseElement.textContent = 'No response yet.';
            }
        }
    });
});
