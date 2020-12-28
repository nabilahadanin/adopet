$(document).ready(function(){
    $("#btn-all").click(function(){
        showPetType("All");
    });
    $("#btn-cats").click(function(){
        showPetType("Cat");
    });
    $("#btn-dogs").click(function(){
        showPetType("Dog");
    });
    $("#btn-others").click(function(){
        showPetType("Other");
    });
    $("#searchpet").change(function(){
        searchPet(document.getElementById("searchpet").value);
    });
    showPetType("All");
});

function searchPet(query) {
    $.getJSON('/list_foto/', function(photos) {
        $.getJSON('/list_hewan/', function(result) {
            let semua_hewan = document.getElementById("all-pet");
            semua_hewan.innerHTML = "";
            result.forEach(hewan => {
                let combinedString = "";
                for (const [key, value] of Object.entries(hewan)) {
                    combinedString += value + " ";
                }
                if (!combinedString.toLowerCase().includes(query.toLowerCase())) {
                    return;
                }
                let foto_hewan = photos.filter(foto => foto.hewan_id === hewan.id);
                let data = document.createElement("div");
                data.classList.add('col-md-4', 'text-center');
                data.innerHTML =
                `<div class="petbox">
                    <div class="pet-photo mx-auto" style="
                        background: url('${ foto_hewan[0].foto }') no-repeat center center;
                        background-size: cover;
                        -webkit-background-size: cover;
                        -moz-background-size: cover;
                        -o-background-size: cover;
                    "></div>
                    <h5 class="pb-1 my-0">${ hewan.nama_hewan }</h5>
                    ${ hewan.kategori } - ${ hewan.usia_hewan }<br>
                    </div>`;
                semua_hewan.appendChild(data);
            });
        });
    });
}

function showPetType(petType) {
    $.getJSON('list_foto/', function(photos) {
        $.getJSON('list_hewan/', function(result) {
            let semua_hewan = document.getElementById("all-pet");
            semua_hewan.innerHTML = "";
            result.forEach(hewan => {
                if (petType !== "All" && hewan.kategori !== petType) {
                    return;
                }
                let foto_hewan = photos.filter(foto => foto.hewan_id === hewan.id);
                let data = document.createElement("div");
                data.classList.add('col-md-4', 'text-center');
                data.innerHTML =
                `<div class="petbox">
                    <div class="pet-photo mx-auto" style="
                        background: url('${ foto_hewan[0].foto }') no-repeat center center;
                        background-size: cover;
                        -webkit-background-size: cover;
                        -moz-background-size: cover;
                        -o-background-size: cover;
                    "></div>
                    <h5 class="pb-1 my-0">${ hewan.nama_hewan }</h5>
                    ${ hewan.kategori } - ${ hewan.usia_hewan }<br>
                </div>`;
                semua_hewan.appendChild(data);
            });
        });
    });
}