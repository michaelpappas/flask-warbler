"use strict";


const $likesBtn = $(".heart-icon")
const $newMessageLink = $("#new-message")


/** changes like button appearance depending on
 * current like status
*/
async function alterLikeStatus(evt) {
  evt.stopImmediatePropagation();
  console.log(evt)
  const id = $(evt.target).attr("id")
  const resp = await axios.post(`/messages/${id}/like`)

  if (resp.status == 200){
    if($(evt.target).attr("class") === "heart-icon bi bi-heart-fill"){
      $(evt.target).attr("class", "heart-icon bi bi-heart")
    }
    else{
      $(evt.target).attr("class", "heart-icon bi bi-heart-fill")
    }
  }
}

// async function newMsg(evt){
//   const resp = await axios.get(`/messages/new`)

// }

// function displayFormInputs(form)

// async function postMsg(){

// }


$likesBtn.on("click", alterLikeStatus)
// $newMessageLink.on("click", newMsg)
// $submitMsg.on("submit", postMsg)
