function checkisDetailedPurchase() {
    if(document.getElementById("id_isDetailedPurchase").checked === true){
        document.getElementById("id_purchaseValue").disabled = true;
    } else {
        document.getElementById("id_purchaseValue").disabled = false;
    }
}