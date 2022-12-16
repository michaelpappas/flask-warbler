"use strict";


const $likesBtn = $(".heart-icon")


/** changes like button appearance depending on
 * current like status
*/
async function alterLikeStatus(evt) {
  evt.preventDefault();
  console.log(evt)
  $id = $(evt.target).attr("id")
  console.log($id)
  const resp = await axios.post(`/messages/{$id}/like`)
}


$likesBtn.on("click", alterLikeStatus)
