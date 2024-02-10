


class Vector {
    constructor(...vals) {
        this.vals = vals;
    }
    map(callback) {
        for (var i = 0; i < this.vals.length; i++) {
            callback(this.vals, i);
        }
        return this;
    }

    round() {
        return this.map((arr, i) => arr[i] = round(arr[i], 10));
    }
    add(v) {
        return this.map((arr, i) => arr[i] += v.vals[i]);
    }
    sub(v) {
        return this.map((arr, i) => arr[i] -= v.vals[i]);
    }
    scale(s) {
        return this.map((arr, i) => arr[i] *= s);
    }
    length() {
        var sum = 0;
        this.map((arr, i) => sum += arr[i] * arr[i]);
        return Math.pow(sum, 0.5);
    }
    setMagnitude(size) {
        return this.normalize().scale(size);
    }
    normalize() {
        return this.scale(1 / this.length());
    }
    to(v) {
        return v.c().sub(this);
    }
    lerp(v, weight) {
        return this.c().add(this.to(v).scale(weight));
    }
    c() {
        return Vector.fromArray(this.vals.slice());
    }
    overwrite(v) {
        return this.map((arr, i) => arr[i] = v.vals[i]);
    }
    dot(v) {
        var sum = 0;
        this.map((arr, i) => sum += arr[i] * v.vals[i]);
        return sum;
    }
    loop(callback) {
        var counter = this.c();
        counter.vals.fill(0);
        while (counter.compare(this) == -1) {
            callback(counter);
            if (counter.incr(this)) {
                break;
            }
        }
    }
    compare(v) {
        for (var i = this.vals.length - 1; i >= 0; i--) {
            if (this.vals[i] < v.vals[i]) {
                continue;
            }
            else if (this.vals[i] == v.vals[i]) {
                return 0;
            }
            else {
                return 1;
            }
        }
        return -1;
    }
    equals(v) {
        for (var i = 0; i < this.vals.length; i++) {
            if (this.vals[i] != v.vals[i]) {
                return false;
            }
        }
        return true;
    }
    incr(comparedTo) {
        for (var i = 0; i < this.vals.length; i++) {
            if ((this.vals[i] + 1) < comparedTo.vals[i]) {
                this.vals[i]++;
                return false;
            }
            else {
                this.vals[i] = 0;
            }
        }
        return true;
    }
    project(v) {
        return v.c().scale(this.dot(v) / v.dot(v));
    }
    get(i) {
        return this.vals[i];
    }
    set(i, val) {
        this.vals[i] = val;
    }
    get x() {
        return this.vals[0];
    }
    get y() {
        return this.vals[1];
    }
    get z() {
        return this.vals[2];
    }
    set x(val) {
        this.vals[0] = val;
    }
    set y(val) {
        this.vals[1] = val;
    }
    set z(val) {
        this.vals[2] = val;
    }
    draw(ctxt) {
        var width = 10;
        var halfwidth = width / 2;
        ctxt.fillRect(this.x - halfwidth, this.y - halfwidth, width, width);
    }
    cross(v) {
        var x = this.y * v.z - this.z * v.y;
        var y = this.z * v.x - this.x * v.z;
        var z = this.x * v.y - this.y * v.x;
        return new Vector(x, y, z);
    }
    static fromArray(vals) {
        var x = new Vector();
        x.vals = vals;
        return x;
    }
    loop2d(callback) {
        var counter = new Vector(0, 0);
        for (counter.x = 0; counter.x < this.x; counter.x++) {
            for (counter.y = 0; counter.y < this.y; counter.y++) {
                callback(counter);
            }
        }
    }
    loop3d(callback) {
        var counter = new Vector(0, 0, 0);
        for (counter.x = 0; counter.x < this.x; counter.x++) {
            for (counter.y = 0; counter.y < this.y; counter.y++) {
                for (counter.z = 0; counter.z < this.z; counter.z++) {
                    callback(counter);
                }
            }
        }
    }
}

class RNG {
    constructor(seed) {
        this.seed = seed;
        this.mod = 4294967296;
        this.multiplier = 1664525;
        this.increment = 1013904223;
    }
    next() {
        this.seed = (this.multiplier * this.seed + this.increment) % this.mod;
        return this.seed;
    }
    norm() {
        return this.next() / this.mod;
    }
    range(min, max) {
        return this.norm() * to(min, max) + min;
    }
}

var TAU = Math.PI * 2;
function map(val, from1, from2, to1, to2) {
    return lerp(to1, to2, inverseLerp(val, from1, from2));
}



function createCanvas(x, y) {
    var canvas = document.createElement('canvas');
    canvas.width = x;
    canvas.height = y;
    canvas.id = 'miCanvas'; // Añadir ID a la etiqueta canvas

    document.body.appendChild(canvas);
    var ctxt = canvas.getContext('2d');
    return { ctxt: ctxt, canvas: canvas };
}

var lastUpdate = Date.now();
function loop(callback) {
    var now = Date.now();
    callback((now - lastUpdate) / 1000);
    lastUpdate = now;
    requestAnimationFrame(() => {
        loop(callback);
    });
}


function findbestIndex(list, evaluator) {
    if (list.length < 1) {
        return -1;
    }
    var bestIndex = 0;
    var bestscore = evaluator(list[0]);
    for (var i = 1; i < list.length; i++) {
        var score = evaluator(list[i]);
        if (score > bestscore) {
            bestscore = score;
            bestIndex = i;
        }
    }
    return bestIndex;
}

function copy2dArray(arr) {
    return create2DArray(get2DArraySize(arr), pos => index2D(arr, pos));
}
function round(number, decimals) {
    var mul = 10 ** decimals;
    return Math.round(number * mul) / mul;
}

function remove(arr, value) {
    var index = arr.indexOf(value);
    if (index > -1) {
        arr.splice(index, 1);
    }
    return arr;
}






class Entity {
    constructor(init) {
        this.id = null;
        this.parent = null;
        this.type = '';
        this.name = '';
        this.children = [];
        // ordercount = 0
        // sortorder = 0
        this.synced = false;
        Object.assign(this, init);
        this.type = 'entity';
    }

    setParent(parent) {
        if (parent == null) {
            this.parent = null;
        }
        else {
            parent.setChild(this);
        }
    }
    getParent() {
        return Entity.globalEntityStore.get(this.parent);
    }


   
}


var colormap = [
    [new Vector(0, 1, 0), 'white'],
    [new Vector(0, 0, -1), 'green'],
    [new Vector(1, 0, 0), 'red'],
    [new Vector(-1, 0, 0), 'orange'],
    [new Vector(0, -1, 0), 'yellow'],
    [new Vector(0, 0, 1), 'blue'],
];
var color2normalmap = {
    'W': new Vector(0, 1, 0),
    'G': new Vector(0, 0, -1),
    'R': new Vector(1, 0, 0),
    'O': new Vector(-1, 0, 0),
    'Y': new Vector(0, -1, 0),
    'B': new Vector(0, 0, 1),
};
var abbrevcolor2colormap = {
    'W': 'white',
    'G': 'green',
    'R': 'red',
    'O': 'orange',
    'Y': 'yellow',
    'B': 'blue',
};
var actionrotate2frontmap = {
    'F': new Vector(1, 0, 0).scale(1),
    'R': new Vector(0, -1, 0).scale(0.25),
    'U': new Vector(1, 0, 0).scale(0.25),
    'L': new Vector(0, 1, 0).scale(0.25),
    'D': new Vector(-1, 0, 0).scale(0.25),
    'B': new Vector(0, 1, 0).scale(0.5),
    'I': new Vector(0, 0, -1).scale(0.5),
    '0': new Vector(0, 1, 0).scale(1),
};
var rotmap = {
    'F': new Vector(0, 0, -1).scale(0.25),
    'R': new Vector(1, 0, 0).scale(0.25),
    'U': new Vector(0, 1, 0).scale(0.25),
    'L': new Vector(-1, 0, 0).scale(0.25),
    'D': new Vector(0, -1, 0).scale(0.25),
    'B': new Vector(0, 0, 1).scale(0.25),
    'F2': new Vector(0, 0, -1).scale(0.5),
    'R2': new Vector(1, 0, 0).scale(0.5),
    'U2': new Vector(0, 1, 0).scale(0.5),
    'L2': new Vector(-1, 0, 0).scale(0.5),
    'D2': new Vector(0, -1, 0).scale(0.5),
    'B2': new Vector(0, 0, 1).scale(0.5),
    "F'": new Vector(0, 0, -1).scale(0.75),
    "R'": new Vector(1, 0, 0).scale(0.75),
    "U'": new Vector(0, 1, 0).scale(0.75),
    "L'": new Vector(-1, 0, 0).scale(0.75),
    "D'": new Vector(0, -1, 0).scale(0.75),
    "B'": new Vector(0, 0, 1).scale(0.75),
};
class CubeLetFace {
    constructor(obj) {
        var _a;
        this.startnormal = (_a = obj === null || obj === void 0 ? void 0 : obj.normal) === null || _a === void 0 ? void 0 : _a.c();
        Object.assign(this, obj);
    }
    getStartPosition2D(cube) {
        return cube.convert3dto2d(this.parent.startpos, this.startnormal);
    }
    getCurrentPosition2D(cube) {
        return cube.convert3dto2d(this.parent.pos, this.normal);
    }
}
class CubeLet {
    constructor(obj) {
        this.faces = [];
        Object.assign(this, obj);
    }
}   
class Cube {
    constructor() {
        this.cubelets = [];
        this.cubeletFaces = [];
        this.history = [];
        this.RNG = new RNG(0);
        this.directionsposmap = [
            [new Vector(0, 0, -1), new Vector(4, 4), Quaternion.fromAxisAngle(new Vector(0, 1, 0).vals, TAU * 0)],
            [new Vector(0, 0, 1), new Vector(10, 4), Quaternion.fromAxisAngle(new Vector(0, 1, 0).vals, TAU * 0.5)],
            [new Vector(0, 1, 0), new Vector(4, 1), Quaternion.fromAxisAngle(new Vector(1, 0, 0).vals, TAU * -0.25)],
            [new Vector(0, -1, 0), new Vector(4, 7), Quaternion.fromAxisAngle(new Vector(1, 0, 0).vals, TAU * 0.25)],
            [new Vector(1, 0, 0), new Vector(7, 4), Quaternion.fromAxisAngle(new Vector(0, 1, 0).vals, TAU * 0.25)],
            [new Vector(-1, 0, 0), new Vector(1, 4), Quaternion.fromAxisAngle(new Vector(0, 1, 0).vals, TAU * -0.25)],
        ];
        this.reset();
    }
    reset() {
        this.history = [];
        this.RNG.seed = 0;
        this.import(`      
        W,W,W,
        W,W,W,
        W,W,W,
  O,O,O,G,G,G,R,R,R,B,B,B,
  O,O,O,G,G,G,R,R,R,B,B,B,
  O,O,O,G,G,G,R,R,R,B,B,B,
        Y,Y,Y,
        Y,Y,Y,
        Y,Y,Y`);
    }
    copy() {
        return new Cube().import(this.export());
    }
    vector2action(vector) {
        var entries = Object.entries(rotmap);
        var i = findbestIndex(entries, ([key, value]) => {
            return -vector.to(value).length();
        });
        return entries[i][0];
    }
    action2vector(action) {
        return rotmap[action].c();
    }
    changePerspective(compositeActions, perspectives) {
        var res = [];
        for (var perspective of perspectives.split(/\s+/)) {
            for (var compositeAction of compositeActions) {
                var rotatedCompositeAction = '';
                for (var action of compositeAction.split(/\s+/)) {
                    var vector = this.action2vector(action);
                    axisRotate(vector, actionrotate2frontmap[perspective], actionrotate2frontmap[perspective].length());
                    rotatedCompositeAction += `${this.vector2action(vector)} `;
                }
                rotatedCompositeAction = rotatedCompositeAction.trim();
                res.push(rotatedCompositeAction);
            }
        }
        return res;
    }

    pathfind2d(dest) {
        var misplacedface = this.cubeletFaces.find(f => f.getStartPosition2D(this).equals(dest));
        var start = this.graph2d.find(k => k.pos.equals(misplacedface.getCurrentPosition2D(this)));
        var goal = this.graph2d.find(k => k.pos.equals(misplacedface.getStartPosition2D(this)));
        return pathfind(start, goal, this.graph2d).map(e => e.data).join(' ');
    }

    apply(rotations, savehistory = true, perspective = 'F') {
        if (rotations) {
            rotations = this.changePerspective([rotations], perspective)[0];
            if (savehistory) {
                this.history = this.history.concat(rotations.split(/\s+/));
            }
            var rots = this.string2rots(rotations);
            for (var rot of rots) {
                this.rot(rot.c().normalize(), rot.length());
            }
        }
        console.log("scram:", rotations)
        return rotations;
    }

    string2rots(input) {
        return input.split(/\s+/).map(op => rotmap[op]);
    }
    rot(faceNormal, turns) {
        var cubelets = this.cubelets.filter(c => c.pos.c().normalize().dot(faceNormal) > 0.1);
        for (var cubelet of cubelets) {
            axisRotate(cubelet.pos, faceNormal, turns);
            for (var cubeletface of cubelet.faces) {
                axisRotate(cubeletface.normal, faceNormal, turns);
            }
        }
    }
    convert3dto2d(pos3d, normal) {
        var [valnormal, offset, quat] = this.directionsposmap.find(vals => vals[0].equals(normal));
        var frontrotated = Vector.fromArray(quat.rotateVector(pos3d.c().vals)).round();
        return new Vector(frontrotated.x + offset.x, frontrotated.y * -1 + offset.y);
    }
 


    getFace(position) {
        return this.cubeletFaces.find(f => f.getCurrentPosition2D(this).equals(position));
    }

    import(data) {
        var colorsgrid = data.trim().split('\n').map(row => row.split(',').filter((cell) => cell != false).map(cell => cell.trim()));
        for (var i of [0, 1, 2, 6, 7, 8]) {
            colorsgrid[i].splice(0, 0, null, null, null);
        }
        this.cubelets = [];
        this.cubeletFaces = [];
        for (var x = -1; x < 2; x++) {
            for (var y = -1; y < 2; y++) {
                for (var z = -1; z < 2; z++) {
                    var normals = [];
                    if (x != 0) {
                        normals.push(new Vector(x, 0, 0));
                    }
                    if (y != 0) {
                        normals.push(new Vector(0, y, 0));
                    }
                    if (z != 0) {
                        normals.push(new Vector(0, 0, z));
                    }
                    var cubelet = new CubeLet({
                        pos: new Vector(x, y, z),
                        startpos: new Vector(0, 0, 0),
                        type: {
                            0: 'core',
                            1: 'center',
                            2: 'edge',
                            3: 'corner',
                        }[normals.length],
                    });
                    this.cubelets.push(cubelet);
                    for (var normal of normals) {
                        var vec2d = this.convert3dto2d(new Vector(x, y, z), normal);
                        var colorabrrev = colorsgrid[vec2d.y][vec2d.x];
                        var startnormal = color2normalmap[colorabrrev];
                        for (var i = 0; i < 3; i++) {
                            if (startnormal.vals[i] != 0) {
                                cubelet.startpos.vals[i] = startnormal.vals[i];
                            }
                        }
                        var newface = new CubeLetFace({
                            color: abbrevcolor2colormap[colorabrrev],
                            parent: cubelet,
                            normal: normal,
                            startnormal: startnormal,
                        });
                        cubelet.faces.push(newface);
                        this.cubeletFaces.push(newface);
                    }
                }
            }
        }
        return this;
    }
   
}


function axisRotate(v, axis, turns) {
    var added = false;
    if (v.vals.length == 2) {
        v.vals.push(0);
        added = true;
    }
    var quat = Quaternion.fromAxisAngle(axis.vals, turns * TAU);
    v.vals = quat.rotateVector(v.vals);
    if (added) {
        v.vals.splice(v.vals.length - 1, 1);
    }
    v.round();
    return v;
}


var gridsize = 50;
var screensize = new Vector(1000, 500);
var { canvas, ctxt } = createCanvas(screensize.x, screensize.y);
var cube = new Cube();
var rngseedelement = document.querySelector('#seedvalue');


loop((dt) => {
    ctxt.fillStyle = '#fdd';
    ctxt.fillRect(0, 0, screensize.x, screensize.y);
    drawCube(cube, ctxt);
});
function drawCube(cube, ctxt) {
    for (var face of cube.cubeletFaces) {
        var pos2d = cube.convert3dto2d(face.parent.pos, face.normal);
        var abs = pos2d.c().scale(gridsize);
        ctxt.fillStyle = face.color;
        ctxt.fillRect(abs.x, abs.y, gridsize, gridsize);

    }
}



























































let timerInterval = 0;
let startTime;
let running = false;
let pressingSpace = false;
let inspeccion = false;

document.addEventListener("keydown", function (event) {
    if (event.key === " ") {
        if (!pressingSpace) {
            pressingSpace = true;
            if (!running) {
                document.getElementById("timer").style.color = "red";
            }
            setTimeout(() => {
                if (pressingSpace && !running) {
                    document.getElementById("timer").style.color = "green";
                    document.getElementById("8").style.color = "green";

                }
            }, 700);
        }
    }
});

document.addEventListener("keyup", function (event) {
    if (event.key === " ") {
        if (pressingSpace) {
            pressingSpace = false;
            const timerColor = document.getElementById("timer").style.color;
            if (timerColor === "green") {
                document.getElementById("timer").style.color = "black";
                startTimer();
            } else if (running) {
                stopTimer();
                updateAVg();   

                setRandomScramble();

            
                updateTimer();
            } else if (!inspeccion) {
                document.getElementById("timer").style.color = "black";
                startInspection();
            }
        }
    }
});     

document.addEventListener("DOMContentLoaded", function () {
    updateAVg();    
    setRandomScramble();


});

function startInspection() {
    if (!running && !inspeccion) {
        inspeccion = true;
        startCountdown();
        document.getElementById("head").style.display = "none";
        document.getElementById("contenedor_lateral").style.display = "none";
        document.getElementById("aos").style.display = "none";
        document.getElementById("contenedor_cubo").style.display = "none";
        document.getElementById("diferencia").style.display = "none";
        document.getElementById("leftbar").style.display = "none";
        document.getElementById("miCanvas").style.display = "none";

        document.getElementById("timer").style.fontSize = "3550%";
        document.getElementById("timer").style.color = "red";

    }
}

function startTimer() {
    if (!running) {
        startTime = new Date().getTime();
        timerInterval = setInterval(updateTimer, 10);
        running = true;
        inspeccion = false;
        document.getElementById("8").style.color = "red";
        document.getElementById("diferencia").style.display = "none";

        document.getElementById("8").style.display = "none";


    }
}

function stopTimer() {
    if (running) {
        clearInterval(timerInterval);
        running = false;
        document.getElementById("head").style.display = "block";
        document.getElementById("aos").style.display = "block";
        document.getElementById("contenedor_lateral").style.display = "block";
        document.getElementById("8").style.display = "none";
        document.getElementById("diferencia").style.display = "block";
        document.getElementById("timer").style.fontSize = "2250%";
        document.getElementById("leftbar").style.display = "block";
        document.getElementById("miCanvas").style.display = "";

        
        document.getElementById("contenedor_cubo").style.display = "";


        const currentTime = new Date().getTime();
        const elapsedTime = (currentTime - startTime) / 1000;
        const scramble = document.getElementById("scramble").textContent;
        saveTime(elapsedTime, scramble);

        updateTimesTable();


    }

}

function updateAVg() {
    $.get("/times", function (data) {
        const ultimoRegistro = data[0];
        const tiempoactual = ultimoRegistro.time_interval !== null ? ultimoRegistro.time_interval : "-";
        const ao5Header = ultimoRegistro.ao5 !== null ? ultimoRegistro.ao5 : "-";
        const ao12Header = ultimoRegistro.ao12 !== null ? ultimoRegistro.ao12 : "-";
        const ao100Header = ultimoRegistro.ao100 !== null ? ultimoRegistro.ao100 : "-";
        // document.getElementById("timer").textContent =  tiempoactual;

        document.getElementById("ao5-header").textContent = ao5Header;
        document.getElementById("ao12-header").textContent =  ao12Header;
        document.getElementById("ao100-header").textContent =  ao100Header;
        document.getElementById("tiempo_actual").textContent =  tiempoactual;
        document.getElementById("ao5").textContent = ao5Header;
        document.getElementById("ao12").textContent =  ao12Header;
        document.getElementById("ao100").textContent =  ao100Header;
    });

    $.get("/mejortiempo", function (data) {
        const ultimoRegistro = data[0];
        const mejor = ultimoRegistro.mejortiempo !== null ? ultimoRegistro.mejortiempo : "-";
        const mejorao5 = ultimoRegistro.ao5 !== null ? ultimoRegistro.mejorao5 : "-";
        const mejorao12 = ultimoRegistro.ao12 !== null ? ultimoRegistro.mejorao12 : "-";
        const mejorao100 = ultimoRegistro.ao100 !== null ? ultimoRegistro.mejorao100 : "-";

        document.getElementById("mejortiempo").textContent =  mejor;
        document.getElementById("mejorao5").textContent = mejorao5;
        document.getElementById("mejorao12").textContent =  mejorao12;
        document.getElementById("mejorao100").textContent =  mejorao100;
    });
    $.get("/get_time_difference", function (data) {
        const diferencia = data;
        const dif = diferencia.difference !== null ? diferencia.difference : "-";
        let dife;
        if(dif>0){
            dife = "(+"+dif+")";
            document.getElementById("diferencia").style.color = "red";

        }else{
            dife = "("+dif+")";
            document.getElementById("diferencia").style.color = "green";

        }
        document.getElementById("diferencia").textContent =  dife;
    });
}

function updateTimesTable() {
    $.get("/times", function (data) {
        document.getElementById("times-body").innerHTML = "";
        data.forEach(function (tiempo) {
            agregarTiempo(tiempo);
        });
    });
}

function saveTime(time, scramble) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/guardar-tiempo", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            console.log("Tiempo guardado exitosamente");
        }
    };
    var data = JSON.stringify({ time: time, scramble: scramble });
    xhr.send(data);
}

function updateTimer() {
    const currentTime = new Date().getTime();
    const elapsedTime = (currentTime - startTime) / 1000;
    const seconds = Math.floor(elapsedTime);
    const milliseconds = Math.floor((elapsedTime - seconds) * 100);
    const firstDecimal = Math.floor(milliseconds / 10); // Obtener solo el primer dígito del decimal
    if (running) {
        document.getElementById("timer").innerHTML = seconds + "<span style='font-size: 250px;'>." + firstDecimal + "</span>";
    } else {
        document.getElementById("timer").innerHTML = seconds + "<span style='font-size: 250px;'>." + (milliseconds < 10 ? "0" + milliseconds : milliseconds) + "</span>";
    }
}
 


function startCountdown() {
    let countdown = 15;

    function updateCountdown() {
        if (!inspeccion) {
            countdown = 15;
            return;
        }
        if (countdown > 0) {
            document.getElementById("timer").textContent = countdown.toFixed();
            countdown -= 0.01;
        }
        if (countdown < 8) {
            document.getElementById("8").style.display = "block";
            
            document.getElementById("8").textContent = "8s!";

        }
        if (countdown < 4) {
            document.getElementById("8").textContent = "Go!!!";
        }
        if (countdown < 1 && document.getElementById("timer").textContent !== "DNF") {
            document.getElementById("timer").textContent = "+2";
            setTimeout(() => {
                if (document.getElementById("timer").textContent === "+2") {
                    document.getElementById("timer").textContent = "DNF";
                }
            }, 2000); // Cambiar a "DNF" después de 2 segundos
        }
    }

  

    // Detener el intervalo después de 15 segundos
    setTimeout(() => {
        clearInterval(countdownInterval);
    }, 15000);



    if (!running) {
        clearInterval(timerInterval);
        document.getElementById("timer").style.color = "black";
        timerInterval = setInterval(updateCountdown, 10);
    }
}

$.get("/times", function (data) {
    data.forEach(function (tiempo) {
        agregarTiempo(tiempo);
    });
});

function agregarTiempo(tiempo) {
    var row = document.createElement("tr");
    var cellIndex = document.createElement("td");
    var cellTime = document.createElement("td");
    var cellAo5 = document.createElement("td");
    var cellAo12 = document.createElement("td");
    cellIndex.textContent = tiempo.indice;
    cellTime.textContent = tiempo.time_interval;
    cellAo5.textContent = tiempo.ao5 !== null ? tiempo.ao5 : "-";
    cellAo12.textContent = tiempo.ao12 !== null ? tiempo.ao12 : "-";
    row.appendChild(cellIndex);
    row.appendChild(cellTime);
    row.appendChild(cellAo5);
    row.appendChild(cellAo12);
    var table = document.getElementById("times-body");
    table.appendChild(row);
}

const moves = ["U", "D", "L", "R", "F", "B"];
const modifiers = ["", "'", "2"];

const forbiddenMoves = {
    "U": ["D", "U'"],
    "D": ["U", "D'"],
    "L": ["R", "L'"],
    "R": ["L", "R'"],
    "F": ["B", "F'"],
    "B": ["F", "B'"]
};

function setRandomScramble() {
    const minLength = 18;
    const maxLength = 21;

    const scrambleLength = Math.floor(Math.random() * (maxLength - minLength + 1)) + minLength;

    let scramble = [];
    let previousMove = "";

    for (let i = 0; i < scrambleLength; i++) {
        let move = getRandomElement(moves);
        while (move === previousMove || isForbiddenMove(previousMove, move)) {
            move = getRandomElement(moves);
        }

        let modifier = getRandomElement(modifiers);
        scramble.push(move + modifier);
        previousMove = move;
    }

    const scrambleString = scramble.join("&nbsp;");
    const scrambleElement = document.getElementById('scramble');
    scrambleElement.innerHTML = scrambleString;
    console.log('scram:', scrambleElement.value );
    console.log('scram:', perspectiveSelect.value) ;
    cube.apply(scrambleElement.value, true, perspectiveSelect.value);
}

function getRandomElement(array) {
    return array[Math.floor(Math.random() * array.length)];
}

function isForbiddenMove(previousMove, currentMove) {
    return previousMove && forbiddenMoves[previousMove].includes(currentMove);
}








