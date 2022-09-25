var sidebar = document.getElementById("sideBar")
function manipularNav() {
    if (sidebar.classList.contains("close")) {
        sidebar.classList.add("open");
        sidebar.classList.remove("close");
        document.getElementById("buttonSideBar").style.marginLeft = "125px";
        document.getElementById("sideBar").style.width = "180px";
        document.getElementById("conteudo").style.marginLeft = "180px";
    } else if (sidebar.classList.contains("open")) {
        sidebar.classList.add("close");
        sidebar.classList.remove("open");
        document.getElementById("buttonSideBar").style.marginLeft = "0";
        document.getElementById("sideBar").style.width = "0";
        document.getElementById("conteudo").style.marginLeft = "10px";
    }
}