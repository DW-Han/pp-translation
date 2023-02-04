chrome.downloads.onChanged.addListener(function(downloadDelta) {
    if (downloadDelta.state && downloadDelta.state.current === 'complete') {

      chrome.windows.create({
        url: "popup.html",
        type: "popup",
        width: 500,
        height: 500
      });


      chrome.downloads.search({id: downloadDelta.id}, function(downloadItems) {
        console.log(downloadItems[0].url);
      });
    }
  });



  chrome.downloads.onChanged.addListener(function(downloadDelta) {
    if (downloadDelta.state) {
      console.log(downloadDelta.state.current);
    }
  });
