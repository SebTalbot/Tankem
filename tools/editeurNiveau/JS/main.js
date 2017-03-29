var ctx = null
var niveau = null
var sizeTuile =50;
var longueurGrid = null;
var hauteurGrid = null;
var debX = null;
var debY = null;
var imgblock1 = new Image()
var imgblock2 = new Image()
var imgblock3 = new Image()
var imgblock4 = new Image()
var imgtree = new Image()
var selector = null;


document.onkeydown = function (e) {
    selector.updatePosition(e)
}

window.onload = function(){

    ctx = document.getElementById("canvas").getContext("2d")
    niveau = new Niveau(12,12)
    document.getElementById("tailleX").value=niveau.tailleX
    document.getElementById("tailleY").value=niveau.tailleY


    imgblock1.src="images/block1.png"
    imgblock2.src="images/block2.jpg"
    imgblock3.src="images/block3.jpg"
    imgblock4.src="images/block4.png"
    imgtree.src="images/treeAlpha.png"

    longueurGrid = sizeTuile * niveau.tailleX;
    hauteurGrid = sizeTuile * niveau.tailleY;
    debX = (document.getElementById("canvas").width - longueurGrid) / 2;
    debY = (document.getElementById("canvas").height - hauteurGrid) / 2;

    selector = new Selector(0,0,sizeTuile);


    tick()
}

function tick(){

    ctx.clearRect(0,0,document.getElementById("canvas").width,document.getElementById("canvas").height)
    drawTiles();
    drawGrid();
    selector.tick();
    for (var i = 0; i < niveau.tabSpawn.length; i++) {
        niveau.tabSpawn[i].tick();
    }

    window.requestAnimationFrame(tick)
}

function drawGrid(){
    ctx.strokeStyle = "black"
    for(var i = 0; i <= niveau.tailleY; ++i){
        ctx.beginPath();
        ctx.moveTo(debX,debY + sizeTuile * i);
        ctx.lineTo(debX + sizeTuile * niveau.tailleX, debY + sizeTuile * i);
        ctx.stroke();
    }
    for(var i = 0; i <= niveau.tailleX; ++i){
        ctx.beginPath();
        ctx.moveTo(debX + sizeTuile * i, debY);
        ctx.lineTo(debX + sizeTuile * i, debY + sizeTuile * niveau.tailleY);
        ctx.stroke();
    }
}

function drawTiles() {
    for(var y = 0; y < niveau.tailleY; ++y){
        for(var x = 0; x < niveau.tailleX; ++x){
            switch(niveau.tabTile[x][y].type){
                case 0:
                    ctx.fillStyle = "grey"
                    ctx.fillRect(debX + x * sizeTuile, debY + y * sizeTuile, sizeTuile, sizeTuile)
                    break
                case 1:
                    ctx.drawImage(imgblock1,debX + x * sizeTuile, debY + y * sizeTuile, sizeTuile, sizeTuile )
                    break
                case 2:
                    ctx.drawImage(imgblock2,debX + x * sizeTuile, debY + y * sizeTuile, sizeTuile, sizeTuile )
                    break
                case 3:
                    ctx.drawImage(imgblock3,debX + x * sizeTuile, debY + y * sizeTuile, sizeTuile, sizeTuile )
                    break
                case 4:
                    ctx.drawImage(imgblock4,debX + x * sizeTuile, debY + y * sizeTuile, sizeTuile, sizeTuile )
                    break
            }
            if(niveau.tabTile[x][y].hasTree){
                ctx.drawImage(imgtree, sizeTuile/4+ debX + x * sizeTuile, sizeTuile/4+ debY + y * sizeTuile, sizeTuile/2, sizeTuile/2)
            }
        }
    }
}

function clickButton(){
    var tailleXinput = parseInt(document.getElementById("tailleX").value)
    var tailleYinput = parseInt(document.getElementById("tailleY").value)
    if(tailleXinput >= 6 && tailleXinput <= 12 && tailleYinput >= 6 && tailleYinput <= 12){
        niveau.setSize(tailleXinput, tailleYinput)
        console.log("tailleX: " + tailleXinput + "  tailleY: " + tailleYinput);
    }
    longueurGrid = sizeTuile * niveau.tailleX;
    hauteurGrid = sizeTuile * niveau.tailleY;
    debX = (document.getElementById("canvas").width - longueurGrid) / 2;
    debY = (document.getElementById("canvas").height - hauteurGrid) / 2;
}

function envoyerTables(){
    var date = new Date();
    date = date.getUTCFullYear() + '-' +
        ('00' + (date.getUTCMonth()+1)).slice(-2) + '-' +
        ('00' + date.getUTCDate()).slice(-2) + ' ' + 
        ('00' + date.getUTCHours()).slice(-2) + ':' + 
        ('00' + date.getUTCMinutes()).slice(-2) + ':' + 
        ('00' + date.getUTCSeconds()).slice(-2);

    var dtoNiveau = new DTONiveau(
        document.getElementById("nomNiveau").value,
        date,
        document.getElementById("status").value,
        niveau.tailleX,
        niveau.tailleY,
        document.getElementById("itemDelMin").value,
        document.getElementById("itemDelMax")
    )

    var tabTuile = [];
    for (var i = 0; i < niveau.tailleX; ++i){
        for(var j = 0; j < niveau.tailleY; ++j){
            if(niveau.tabTile[i][j].type != 0){
                tabTuile.push(new DTOTuile(niveau.tabTile[i][j].x,niveau.tabTile[i][j].y,niveau.tabTile[i][j].type,niveau.tabTile[i][j].hasTree));
            }
        }
    }

}
