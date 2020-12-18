$(document).ready(function(){
    $("#filter-all").click(function(){
        showPetType("All");
    });
    $("#filter-cats").click(function(){
        showPetType("Cat");
    });
    $("#filter-dogs").click(function(){
        showPetType("Dog");
    });
    $("#filter-others").click(function(){
        showPetType("Other");
    });
    $("#searchpet").change(function(){
        searchPet(document.getElementById("searchpet").value);
    });
    showPetType("All");
});

function searchPet(query) {
    $.getJSON('/list_photo/', function(photos) {
        $.getJSON('/list_pet/', function(result) {
            let allPet = document.getElementById("all-pet");
            allPet.innerHTML = "";
            result.forEach(pet => {
                let combinedString = "";
                for (const [key, value] of Object.entries(pet)) {
                    combinedString += value + " ";
                }
                if (!combinedString.toLowerCase().includes(query.toLowerCase())) {
                    return;
                }
                let petPhoto = photos.filter(photo => photo.pet_id === pet.id);
                let data = document.createElement("div");
                data.classList.add('col-md-4', 'text-center');
                data.innerHTML =
                `<div class="petbox">
                    <div class="pet-photo mx-auto" style="
                        background: url('${ petPhoto[0].photo }') no-repeat center center;
                        background-size: cover;
                        -webkit-background-size: cover;
                        -moz-background-size: cover;
                        -o-background-size: cover;
                    "></div>
                    <h5 class="pb-1 my-0">${ pet.pet_name }</h5>
                    ${ pet.pet_type } - ${ pet.pet_age } - ${ pet.pet_breed }<br>
                    ${/*${ pet.owner_city }, ${ pet.owner_country }</i><br>*/''}
                    <a href="/detail/${ pet.id }/"><button type="button" class="btn white-btn w-75 mt-2">More info</button></a>
                </div>`;
                allPet.appendChild(data);
            });
        });
    });
}

function showPetType(petType) {
    $.getJSON('/list_photo/', function(photos) {
        $.getJSON('/list_pet/', function(result) {
            let allPet = document.getElementById("all-pet");
            allPet.innerHTML = "";
            result.forEach(pet => {
                if (petType !== "All" && pet.pet_type !== petType) {
                    return;
                }
                let petPhoto = photos.filter(photo => photo.pet_id === pet.id);
                let data = document.createElement("div");
                data.classList.add('col-md-4', 'text-center');
                data.innerHTML =
                `<div class="petbox">
                    <div class="pet-photo mx-auto" style="
                        background: url('${ petPhoto[0].photo }') no-repeat center center;
                        background-size: cover;
                        -webkit-background-size: cover;
                        -moz-background-size: cover;
                        -o-background-size: cover;
                    "></div>
                    <h5 class="pb-1 my-0">${ pet.pet_name }</h5>
                    ${ pet.pet_type } - ${ pet.pet_age } - ${ pet.pet_breed }<br>
                    ${/*${ pet.owner_city }, ${ pet.owner_country }</i><br>*/''}
                    <a href="/detail/${ pet.id }/"><button type="button" class="btn white-btn w-75 mt-2">More info</button></a>
                </div>`;
                allPet.appendChild(data);
            });
        });
    });
}
