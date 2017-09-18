function initPageDevide(pageId, footerId, pageNum) {
  // initialize
  $("div[id^='" + pageId + "']").hide(); // hide all
  $('#' + pageId + '1').show(); // show the first
  var footerSet = $("li[id^='" + footerId + "']");
  var pageSet = $("div[id^='" + pageId + "']");
  footerSet.each(function() {
    $(this).click(function() {
      getCurrentHideandShow($(this).children().html(), pageNum, pageId, pageSet, footerId);
    });
  });
}


function getCurrentHideandShow(pageindex, totalPageNum, pageId, pageSet, footerId) {
  var currentPageNum, nextPageNum;
  pageSet.each(function() {
    if ($(this).css('display') !== 'none') {
      currentPageNum = $(this).attr('id').slice(pageId.length);
      currentPageNum = parseInt(currentPageNum);
      if (pageindex === '«') {
        if (currentPageNum === 1) {
          // do nothing
          nextPageNum = currentPageNum;
        } else {
          // hide the current page
          nextPageNum = currentPageNum - 1;
          $(this).hide();
        }
      } else if (pageindex === '»') {
        console.log(currentPageNum);
        if (currentPageNum === totalPageNum) {
          // do nothing
          nextPageNum = currentPageNum;
        } else {
          // hide the current page
          nextPageNum = currentPageNum + 1;
          $(this).hide();

        }
      } else {
        // hide the current page
        nextPageNum = parseInt(pageindex);
        $(this).hide();
      }
      $('#' + pageId + String(nextPageNum)).show();
      var footer_current = $('#' + footerId + String(currentPageNum));
      console.log(footer_current.children().css('background-color', '#fafafa'));

      var footer_next = $('#' + footerId + String(nextPageNum));
      console.log(footer_next.children().css('background-color', '#dfdfdf'));
      // console.log(html1);

      // add return false to break the each
      return false;

    }
  });
};
