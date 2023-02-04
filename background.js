chrome.downloads.onChanged.addListener(function(downloadDelta) {
    if (downloadDelta.state && downloadDelta.state.current === 'complete') {

      // getting last download and checking if its a power point
      chrome.downloads.search({id: downloadDelta.id}, function(downloadItems) {
        console.log(downloadItems[0].url);
        if (downloadItems[0].filename.endsWith('.pptx')) {
          console.log(downloadItems[0].filename + ' is a PowerPoint presentation.');

          chrome.windows.create({
            url: "popup.html",
            type: "popup",
            width: 500,
            height: 500
          });

        } else {
          console.log(downloadItems[0].filename + ' is not a PowerPoint presentation.');
        }
      });

      chrome.downloads.search({}, function(downloadItems) {
        downloadItems.forEach(function(downloadItem) {
          
        });
      });

      
    }
  });



  chrome.downloads.onChanged.addListener(function(downloadDelta) {
    if (downloadDelta.state) {
      console.log(downloadDelta.state.current);
    }
  });
