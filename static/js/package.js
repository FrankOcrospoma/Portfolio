// class Vector {
//     constructor(...vals) {
//         this.vals = vals;
//     }
//     map(callback) {
//         for (var i = 0; i < this.vals.length; i++) {
//             callback(this.vals, i);
//         }
//         return this;
//     }
//     mul(v) {
//         return this.map((arr, i) => arr[i] *= v.vals[i]);
//     }
//     div(v) {
//         return this.map((arr, i) => arr[i] /= v.vals[i]);
//     }
//     floor() {
//         return this.map((arr, i) => arr[i] = Math.floor(arr[i]));
//     }
//     ceil() {
//         return this.map((arr, i) => arr[i] = Math.ceil(arr[i]));
//     }
//     round() {
//         return this.map((arr, i) => arr[i] = round(arr[i], 10));
//     }
//     add(v) {
//         return this.map((arr, i) => arr[i] += v.vals[i]);
//     }
//     sub(v) {
//         return this.map((arr, i) => arr[i] -= v.vals[i]);
//     }
//     scale(s) {
//         return this.map((arr, i) => arr[i] *= s);
//     }
//     length() {
//         var sum = 0;
//         this.map((arr, i) => sum += arr[i] * arr[i]);
//         return Math.pow(sum, 0.5);
//     }
//     setMagnitude(size) {
//         return this.normalize().scale(size);
//     }
//     normalize() {
//         return this.scale(1 / this.length());
//     }
//     to(v) {
//         return v.c().sub(this);
//     }
//     lerp(v, weight) {
//         return this.c().add(this.to(v).scale(weight));
//     }
//     c() {
//         return Vector.fromArray(this.vals.slice());
//     }
//     overwrite(v) {
//         return this.map((arr, i) => arr[i] = v.vals[i]);
//     }
//     dot(v) {
//         var sum = 0;
//         this.map((arr, i) => sum += arr[i] * v.vals[i]);
//         return sum;
//     }
//     loop(callback) {
//         var counter = this.c();
//         counter.vals.fill(0);
//         while (counter.compare(this) == -1) {
//             callback(counter);
//             if (counter.incr(this)) {
//                 break;
//             }
//         }
//     }
//     compare(v) {
//         for (var i = this.vals.length - 1; i >= 0; i--) {
//             if (this.vals[i] < v.vals[i]) {
//                 continue;
//             }
//             else if (this.vals[i] == v.vals[i]) {
//                 return 0;
//             }
//             else {
//                 return 1;
//             }
//         }
//         return -1;
//     }
//     equals(v) {
//         for (var i = 0; i < this.vals.length; i++) {
//             if (this.vals[i] != v.vals[i]) {
//                 return false;
//             }
//         }
//         return true;
//     }
//     incr(comparedTo) {
//         for (var i = 0; i < this.vals.length; i++) {
//             if ((this.vals[i] + 1) < comparedTo.vals[i]) {
//                 this.vals[i]++;
//                 return false;
//             }
//             else {
//                 this.vals[i] = 0;
//             }
//         }
//         return true;
//     }
//     project(v) {
//         return v.c().scale(this.dot(v) / v.dot(v));
//     }
//     get(i) {
//         return this.vals[i];
//     }
//     set(i, val) {
//         this.vals[i] = val;
//     }
//     get x() {
//         return this.vals[0];
//     }
//     get y() {
//         return this.vals[1];
//     }
//     get z() {
//         return this.vals[2];
//     }
//     set x(val) {
//         this.vals[0] = val;
//     }
//     set y(val) {
//         this.vals[1] = val;
//     }
//     set z(val) {
//         this.vals[2] = val;
//     }
//     draw(ctxt) {
//         var width = 10;
//         var halfwidth = width / 2;
//         ctxt.fillRect(this.x - halfwidth, this.y - halfwidth, width, width);
//     }
//     cross(v) {
//         var x = this.y * v.z - this.z * v.y;
//         var y = this.z * v.x - this.x * v.z;
//         var z = this.x * v.y - this.y * v.x;
//         return new Vector(x, y, z);
//     }
//     static fromArray(vals) {
//         var x = new Vector();
//         x.vals = vals;
//         return x;
//     }
//     loop2d(callback) {
//         var counter = new Vector(0, 0);
//         for (counter.x = 0; counter.x < this.x; counter.x++) {
//             for (counter.y = 0; counter.y < this.y; counter.y++) {
//                 callback(counter);
//             }
//         }
//     }
//     loop3d(callback) {
//         var counter = new Vector(0, 0, 0);
//         for (counter.x = 0; counter.x < this.x; counter.x++) {
//             for (counter.y = 0; counter.y < this.y; counter.y++) {
//                 for (counter.z = 0; counter.z < this.z; counter.z++) {
//                     callback(counter);
//                 }
//             }
//         }
//     }
// }

// class RNG {
//     constructor(seed) {
//         this.seed = seed;
//         this.mod = 4294967296;
//         this.multiplier = 1664525;
//         this.increment = 1013904223;
//     }
//     next() {
//         this.seed = (this.multiplier * this.seed + this.increment) % this.mod;
//         return this.seed;
//     }
//     norm() {
//         return this.next() / this.mod;
//     }
//     range(min, max) {
//         return this.norm() * to(min, max) + min;
//     }
// }
// class Store {
//     constructor() {
//         this.map = new Map();
//         this.counter = 0;
//     }
//     get(id) {
//         return this.map.get(id);
//     }
//     add(item) {
//         item.id = this.counter++;
//         this.map.set(item.id, item);
//     }
//     list() {
//         return Array.from(this.map.values());
//     }
//     remove(id) {
//         var val = this.map.get(id);
//         this.map.delete(id);
//         return val;
//     }
// }
// var TAU = Math.PI * 2;
// function map(val, from1, from2, to1, to2) {
//     return lerp(to1, to2, inverseLerp(val, from1, from2));
// }
// function inverseLerp(val, a, b) {
//     return to(a, val) / to(a, b);
// }
// function inRange(min, max, value) {
//     if (min > max) {
//         var temp = min;
//         min = max;
//         max = temp;
//     }
//     return value <= max && value >= min;
// }
// function min(a, b) {
//     if (a < b)
//         return a;
//     return b;
// }
// function max(a, b) {
//     if (a > b)
//         return a;
//     return b;
// }
// function clamp(val, min, max) {
//     return this.max(this.min(val, max), min);
// }
// function rangeContain(a1, a2, b1, b2) {
//     return max(a1, a2) >= max(b1, b2) && min(a1, a2) <= max(b1, b2);
// }
// function startMouseListen(localcanvas) {
//     var mousepos = new Vector(0, 0);
//     document.addEventListener('mousemove', (e) => {
//         mousepos.overwrite(getMousePos(localcanvas, e));
//     });
//     return mousepos;
// }
// function getMousePos(canvas, evt) {
//     var rect = canvas.getBoundingClientRect();
//     return new Vector(evt.clientX - rect.left, evt.clientY - rect.top);
// }
// function createCanvas(x, y) {
//     var canvas = document.createElement('canvas');
//     canvas.width = x;
//     canvas.height = y;
//     canvas.id = 'miCanvas'; // Añadir ID a la etiqueta canvas

//     document.body.appendChild(canvas);
//     var ctxt = canvas.getContext('2d');
//     return { ctxt: ctxt, canvas: canvas };
// }
// function random(min, max) {
//     return Math.random() * (max - min) + min;
// }
// var lastUpdate = Date.now();
// function loop(callback) {
//     var now = Date.now();
//     callback((now - lastUpdate) / 1000);
//     lastUpdate = now;
//     requestAnimationFrame(() => {
//         loop(callback);
//     });
// }
// function mod(number, modulus) {
//     return ((number % modulus) + modulus) % modulus;
// }
// var keys = {};
// document.addEventListener('keydown', (e) => {
//     keys[e.key] = true;
// });
// document.addEventListener('keyup', (e) => {
//     keys[e.key] = false;
// });
// function getMoveInput() {
//     var dir = new Vector(0, 0);
//     if (keys['a'])
//         dir.x--; //left
//     if (keys['w'])
//         dir.y++; //up
//     if (keys['d'])
//         dir.x++; //right
//     if (keys['s'])
//         dir.y--; //down
//     return dir;
// }
// function getMoveInputYFlipped() {
//     var input = getMoveInput();
//     input.y *= -1;
//     return input;
// }
// function loadTextFiles(strings) {
//     var promises = [];
//     for (var string of strings) {
//         var promise = fetch(string)
//             .then(resp => resp.text())
//             .then(text => text);
//         promises.push(promise);
//     }
//     return Promise.all(promises);
// }
// function loadImages(urls) {
//     var promises = [];
//     for (var url of urls) {
//         promises.push(new Promise((res, rej) => {
//             var image = new Image();
//             image.onload = e => {
//                 res(image);
//             };
//             image.src = url;
//         }));
//     }
//     return Promise.all(promises);
// }
// function findbestIndex(list, evaluator) {
//     if (list.length < 1) {
//         return -1;
//     }
//     var bestIndex = 0;
//     var bestscore = evaluator(list[0]);
//     for (var i = 1; i < list.length; i++) {
//         var score = evaluator(list[i]);
//         if (score > bestscore) {
//             bestscore = score;
//             bestIndex = i;
//         }
//     }
//     return bestIndex;
// }
// function string2html(string) {
//     var div = document.createElement('div');
//     div.innerHTML = string;
//     return div.children[0];
// }
// function lerp(a, b, r) {
//     return a + to(a, b) * r;
// }
// function to(a, b) {
//     return b - a;
// }
// function swap(arr, a = 0, b = 1) {
//     var temp = arr[a];
//     arr[a] = arr[b];
//     arr[b] = temp;
// }
// function first(arr) {
//     return arr[0];
// }
// function last(arr) {
//     return arr[arr.length - 1];
// }
// function create2DArray(size, filler) {
//     var result = new Array(size.y);
//     for (var i = 0; i < size.y; i++) {
//         result[i] = new Array(size.x);
//     }
//     size.loop2d(v => {
//         result[v.y][v.x] = filler(v);
//     });
//     return result;
// }
// function get2DArraySize(arr) {
//     return new Vector(arr[0].length, arr.length);
// }
// function index2D(arr, i) {
//     return arr[i.x][i.y];
// }
// function copy2dArray(arr) {
//     return create2DArray(get2DArraySize(arr), pos => index2D(arr, pos));
// }
// function round(number, decimals) {
//     var mul = 10 ** decimals;
//     return Math.round(number * mul) / mul;
// }
// var rng = new RNG(0);
// function shuffle(array) {
//     var currentIndex = array.length, temporaryValue, randomIndex;
//     while (0 !== currentIndex) {
//         randomIndex = Math.floor(rng.norm() * currentIndex);
//         currentIndex -= 1;
//         temporaryValue = array[currentIndex];
//         array[currentIndex] = array[randomIndex];
//         array[randomIndex] = temporaryValue;
//     }
//     return array;
// }
// function remove(arr, value) {
//     var index = arr.indexOf(value);
//     if (index > -1) {
//         arr.splice(index, 1);
//     }
//     return arr;
// }
// class StopWatch {
//     constructor() {
//         this.starttimestamp = Date.now();
//         this.pausetimestamp = Date.now();
//         this.pausetime = 0;
//         this.paused = true;
//     }
//     get() {
//         var currentamountpaused = 0;
//         if (this.paused) {
//             currentamountpaused = to(this.pausetimestamp, Date.now());
//         }
//         return to(this.starttimestamp, Date.now()) - (this.pausetime + currentamountpaused);
//     }
//     start() {
//         this.paused = false;
//         this.starttimestamp = Date.now();
//         this.pausetime = 0;
//     }
//     continue() {
//         if (this.paused) {
//             this.paused = false;
//             this.pausetime += to(this.pausetimestamp, Date.now());
//         }
//     }
//     pause() {
//         if (this.paused == false) {
//             this.paused = true;
//             this.pausetimestamp = Date.now();
//         }
//     }
//     reset() {
//         this.paused = true;
//         this.starttimestamp = Date.now();
//         this.pausetimestamp = Date.now();
//         this.pausetime = 0;
//     }
// }
// class Rule {
//     constructor(message, cb) {
//         this.message = message;
//         this.cb = cb;
//     }
// }
// class Ability {
//     constructor(cb) {
//         this.cb = cb;
//         // ammo:number = 1
//         // maxammo:number = 1
//         // ammorechargerate:number = 1000
//         // casttime:number = 2000
//         // channelduration:number = 3000
//         this.cooldown = 1000;
//         this.lastfire = Date.now();
//         this.rules = [
//             new Rule('not ready yet', () => (this.lastfire + this.cooldown) < Date.now()),
//         ];
//         this.stopwatch = new StopWatch();
//         this.ventingtime = 0;
//         this.onCastFinished = new EventSystem();
//         this.shots = 0;
//         this.firing = false;
//     }
//     //positive if you need to wait 0 or negative if you can call it
//     timeTillNextPossibleActivation() {
//         return to(Date.now(), this.lastfire + this.cooldown);
//     }
//     canActivate() {
//         return this.rules.every(r => r.cb());
//     }
//     callActivate() {
//         this.cb();
//     }
//     fire() {
//         if (this.firing == false) {
//             this.startfire();
//         }
//         else {
//             this.holdfire();
//         }
//     }
//     releasefire() {
//         this.firing = false;
//     }
//     tapfire() {
//         this.startfire();
//         this.releasefire();
//     }
//     startfire() {
//         if (this.rules.some(r => r.cb())) {
//             this.firing = true;
//             this.ventingtime = 0;
//             this.stopwatch.start();
//             this.ventingtime -= this.cooldown;
//             this.shots = 1;
//             this.lastfire = Date.now();
//             this.cb();
//         }
//     }
//     holdfire() {
//         this.ventingtime += this.stopwatch.get();
//         this.stopwatch.start();
//         this.shots = Math.ceil(this.ventingtime / this.cooldown);
//         this.ventingtime -= this.shots * this.cooldown;
//         this.lastfire = Date.now();
//         if (this.shots > 0) {
//             this.cb();
//         }
//     }
// }
// var AnimType;
// (function (AnimType) {
//     AnimType[AnimType["once"] = 0] = "once";
//     AnimType[AnimType["repeat"] = 1] = "repeat";
//     AnimType[AnimType["pingpong"] = 2] = "pingpong";
//     AnimType[AnimType["extend"] = 3] = "extend";
// })(AnimType || (AnimType = {}));
// class Anim {
//     constructor() {
//         this.animType = AnimType.once;
//         this.reverse = false;
//         this.duration = 1000;
//         this.stopwatch = new StopWatch();
//         this.begin = 0;
//         this.end = 1;
//     }
//     get() {
//         var cycles = this.stopwatch.get() / this.duration;
//         switch (this.animType) {
//             case AnimType.once:
//                 return clamp(lerp(this.begin, this.end, cycles), this.begin, this.end);
//             case AnimType.repeat:
//                 return lerp(this.begin, this.end, mod(cycles, 1));
//             case AnimType.pingpong:
//                 var pingpongcycle = mod(cycles, 2);
//                 if (pingpongcycle <= 1) {
//                     return lerp(this.begin, this.end, pingpongcycle);
//                 }
//                 else {
//                     return lerp(this.end, this.begin, pingpongcycle - 1);
//                 }
//             case AnimType.extend:
//                 var distPerCycle = to(this.begin, this.end);
//                 return Math.floor(cycles) * distPerCycle + lerp(this.begin, this.end, mod(cycles, 1));
//         }
//     }
// }
// class Rect {
//     constructor(min, max) {
//         this.min = min;
//         this.max = max;
//     }
//     collidePoint(point) {
//         for (var i = 0; i < this.min.vals.length; i++) {
//             if (!inRange(this.min.vals[i], this.max.vals[i], point.vals[i])) {
//                 return false;
//             }
//         }
//         return true;
//     }
//     size() {
//         return this.min.to(this.max);
//     }
//     collideBox(other) {
//         for (var i = 0; i < 2; i++) {
//             if (!rangeOverlap(this.min[i], this.max[i], other.min[i], other.max[i])) {
//                 return false;
//             }
//         }
//         return true;
//     }
//     getPoint(relativePos) {
//         return this.min.c().add(this.size().mul(relativePos));
//     }
//     draw(ctxt) {
//         var size = this.size();
//         ctxt.fillRect(this.min.x, this.min.y, size.x, size.y);
//     }
//     move(pos) {
//         var size = this.size();
//         this.min = pos;
//         this.max = this.min.c().add(size);
//     }
//     loop(callback) {
//         var temp = this.max.c();
//         this.size().loop(v2 => {
//             temp.overwrite(v2);
//             temp.add(this.min);
//             callback(temp);
//         });
//     }
// }
// function rangeOverlap(range1A, range1B, range2A, range2B) {
//     return range1A <= range2B && range2A <= range1B;
// }
// class EventQueue {
//     constructor() {
//         this.idcounter = 0;
//         this.onProcessFinished = new EventSystem();
//         this.onRuleBroken = new EventSystem();
//         this.rules = [];
//         this.discoveryidcounter = 0;
//         this.listeners = [];
//         this.events = [];
//     }

//     listenDiscovery(type, cb) {
//         this.listen(type, (discovery) => {
//             cb(discovery.data, discovery.id);
//         });
//     }
//     startDiscovery(type, data, cb) {
//         let createdid = this.discoveryidcounter++;
//         let listenerid = this.listen('completediscovery', (discovery) => {
//             if (discovery.data.id == createdid) {
//                 this.unlisten(listenerid);
//                 cb(discovery.data.data);
//             }
//         });
//         this.addAndTrigger(type, { data, id: createdid });
//     }
//     completeDiscovery(data, id) {
//         this.addAndTrigger('completediscovery', { data, id });
//     }
//     listen(type, cb) {
//         var id = this.idcounter++;
//         this.listeners.push({
//             id: id,
//             type: type,
//             cb,
//         });
//         return id;
//     }
//     listenOnce(type, cb) {
//         let id = this.listen(type, (data) => {
//             this.unlisten(id);
//             cb(data);
//         });
//         return id;
//     }
//     unlisten(id) {
//         var index = this.listeners.findIndex(o => o.id == id);
//         this.listeners.splice(index, 1);
//     }
//     process() {
//         while (this.events.length > 0) {
//             let currentEvent = this.events.shift();
//             let listeners = this.listeners.filter(l => l.type == currentEvent.type);
//             let brokenrules = this.rules.filter(r => r.type == currentEvent.type && r.rulecb(currentEvent.data) == false);
//             if (brokenrules.length == 0) {
//                 for (let listener of listeners) {
//                     listener.cb(currentEvent.data);
//                 }
//             }
//             else {
//                 console.log(first(brokenrules).error);
//                 this.onRuleBroken.trigger({ event: currentEvent, error: first(brokenrules).error });
//             }
//         }
//         this.onProcessFinished.trigger(0);
//     }
//     add(type, data) {
//         this.events.push({
//             type: type,
//             data: data,
//         });
//     }
//     addAndTrigger(type, data) {
//         this.add(type, data);
//         this.process();
//     }
//     addRule(type, error, rulecb) {
//         this.rules.push({ type, error, rulecb });
//     }
// }
// class EventSystem {
//     constructor() {
//         this.idcounter = 0;
//         this.listeners = [];
//     }
//     listen(cb) {
//         var listener = {
//             id: this.idcounter++,
//             cb: cb,
//         };
//         this.listeners.push(listener);
//         return listener.id;
//     }
//     unlisten(id) {
//         var index = this.listeners.findIndex(o => o.id == id);
//         this.listeners.splice(index, 1);
//     }
//     trigger(val) {
//         for (var listener of this.listeners) {
//             listener.cb(val);
//         }
//     }
// }
// class Camera {
//     constructor(ctxt) {
//         this.ctxt = ctxt;
//         this.pos = new Vector(0, 0);
//         this.scale = new Vector(1, 1);
//     }
//     begin() {
//         ctxt.save();
//         var m = this.createMatrixScreen2World().inverse();
//         ctxt.transform(m.a, m.b, m.c, m.d, m.e, m.f);
//     }
//     end() {
//         ctxt.restore();
//     }
//     createMatrixScreen2World() {
//         var a = new DOMMatrix([
//             1, 0, 0, 1, -screensize.x / 2, -screensize.y / 2
//         ]);
//         var b = new DOMMatrix([
//             this.scale.x, 0, 0, this.scale.y, this.pos.x, this.pos.y
//         ]);
//         return b.multiply(a);
//     }
//     screen2world(pos) {
//         var dompoint = this.createMatrixScreen2World().transformPoint(new DOMPoint(pos.x, pos.y));
//         return new Vector(dompoint.x, dompoint.y);
//     }
//     world2screen(pos) {
//         var dompoint = this.createMatrixScreen2World().inverse().transformPoint(new DOMPoint(pos.x, pos.y));
//         return new Vector(dompoint.x, dompoint.y);
//     }
// }
// class Entity {
//     constructor(init) {
//         this.id = null;
//         this.parent = null;
//         this.type = '';
//         this.name = '';
//         this.children = [];
//         // ordercount = 0
//         // sortorder = 0
//         this.synced = false;
//         Object.assign(this, init);
//         this.type = 'entity';
//     }
//     setChild(child) {
//         //remove child from old parent
//         var oldparent = Entity.globalEntityStore.get(child.parent);
//         if (oldparent != null) {
//             remove(oldparent.children, child.id);
//         }
//         this.children.push(child.id);
//         child.parent = this.id;
//         // child.sortorder = this.ordercount++
//     }
//     setParent(parent) {
//         if (parent == null) {
//             this.parent = null;
//         }
//         else {
//             parent.setChild(this);
//         }
//     }
//     getParent() {
//         return Entity.globalEntityStore.get(this.parent);
//     }
//     descendant(cb) {
//         return this.descendants(cb)[0];
//     }
//     descendants(cb) {
//         var children = this._children(cb);
//         var grandchildren = children.flatMap(c => c.descendants(cb));
//         return children.concat(grandchildren);
//     }
//     child(cb) {
//         return this._children(cb)[0];
//     }
//     _children(cb) {
//         return this.children.map(id => Entity.globalEntityStore.get(id)).filter(cb);
//     }
//     allChildren() {
//         return this._children(() => true);
//     }
//     remove() {
//         remove(this.getParent().children, this.id);
//         Entity.globalEntityStore.remove(this.id);
//         this.removeChildren();
//         return this;
//     }
//     inject(parent) {
//         Entity.globalEntityStore.add(this);
//         this.setParent(parent);
//         return this;
//     }
//     removeChildren() {
//         this.descendants(() => true).forEach(e => Entity.globalEntityStore.remove(e.id));
//         this.children = [];
//     }
//     ancestor(cb) {
//         var current = this;
//         while (current != null && cb(current) == false) {
//             current = Entity.globalEntityStore.get(current.parent);
//         }
//         return current;
//     }
// }
// class Player extends Entity {
//     constructor(init) {
//         super();
//         this.disconnected = false;
//         this.dctimestamp = 0;
//         Object.assign(this, init);
//         this.type = 'player';
//     }
// }

// var colormap = [
//     [new Vector(0, 1, 0), 'white'],
//     [new Vector(0, 0, -1), 'green'],
//     [new Vector(1, 0, 0), 'red'],
//     [new Vector(-1, 0, 0), 'orange'],
//     [new Vector(0, -1, 0), 'yellow'],
//     [new Vector(0, 0, 1), 'blue'],
// ];
// var color2normalmap = {
//     'W': new Vector(0, 1, 0),
//     'G': new Vector(0, 0, -1),
//     'R': new Vector(1, 0, 0),
//     'O': new Vector(-1, 0, 0),
//     'Y': new Vector(0, -1, 0),
//     'B': new Vector(0, 0, 1),
// };
// var abbrevcolor2colormap = {
//     'W': 'white',
//     'G': 'green',
//     'R': 'red',
//     'O': 'orange',
//     'Y': 'yellow',
//     'B': 'blue',
// };
// var actionrotate2frontmap = {
//     'F': new Vector(1, 0, 0).scale(1),
//     'R': new Vector(0, -1, 0).scale(0.25),
//     'U': new Vector(1, 0, 0).scale(0.25),
//     'L': new Vector(0, 1, 0).scale(0.25),
//     'D': new Vector(-1, 0, 0).scale(0.25),
//     'B': new Vector(0, 1, 0).scale(0.5),
//     'I': new Vector(0, 0, -1).scale(0.5),
//     '0': new Vector(0, 1, 0).scale(1),
// };
// var rotmap = {
//     'F': new Vector(0, 0, -1).scale(0.25),
//     'R': new Vector(1, 0, 0).scale(0.25),
//     'U': new Vector(0, 1, 0).scale(0.25),
//     'L': new Vector(-1, 0, 0).scale(0.25),
//     'D': new Vector(0, -1, 0).scale(0.25),
//     'B': new Vector(0, 0, 1).scale(0.25),
//     'F2': new Vector(0, 0, -1).scale(0.5),
//     'R2': new Vector(1, 0, 0).scale(0.5),
//     'U2': new Vector(0, 1, 0).scale(0.5),
//     'L2': new Vector(-1, 0, 0).scale(0.5),
//     'D2': new Vector(0, -1, 0).scale(0.5),
//     'B2': new Vector(0, 0, 1).scale(0.5),
//     "F'": new Vector(0, 0, -1).scale(0.75),
//     "R'": new Vector(1, 0, 0).scale(0.75),
//     "U'": new Vector(0, 1, 0).scale(0.75),
//     "L'": new Vector(-1, 0, 0).scale(0.75),
//     "D'": new Vector(0, -1, 0).scale(0.75),
//     "B'": new Vector(0, 0, 1).scale(0.75),
// };
// class CubeLetFace {
//     constructor(obj) {
//         var _a;
//         this.startnormal = (_a = obj === null || obj === void 0 ? void 0 : obj.normal) === null || _a === void 0 ? void 0 : _a.c();
//         Object.assign(this, obj);
//     }
//     getStartPosition2D(cube) {
//         return cube.convert3dto2d(this.parent.startpos, this.startnormal);
//     }
//     getCurrentPosition2D(cube) {
//         return cube.convert3dto2d(this.parent.pos, this.normal);
//     }
// }
// class CubeLet {
//     constructor(obj) {
//         this.faces = [];
//         Object.assign(this, obj);
//     }
// }
// class Cube {
//     constructor() {
//         this.cubelets = [];
//         this.cubeletFaces = [];
//         this.history = [];
//         this.RNG = new RNG(0);
//         this.directionsposmap = [
//             [new Vector(0, 0, -1), new Vector(4, 4), Quaternion.fromAxisAngle(new Vector(0, 1, 0).vals, TAU * 0)],
//             [new Vector(0, 0, 1), new Vector(10, 4), Quaternion.fromAxisAngle(new Vector(0, 1, 0).vals, TAU * 0.5)],
//             [new Vector(0, 1, 0), new Vector(4, 1), Quaternion.fromAxisAngle(new Vector(1, 0, 0).vals, TAU * -0.25)],
//             [new Vector(0, -1, 0), new Vector(4, 7), Quaternion.fromAxisAngle(new Vector(1, 0, 0).vals, TAU * 0.25)],
//             [new Vector(1, 0, 0), new Vector(7, 4), Quaternion.fromAxisAngle(new Vector(0, 1, 0).vals, TAU * 0.25)],
//             [new Vector(-1, 0, 0), new Vector(1, 4), Quaternion.fromAxisAngle(new Vector(0, 1, 0).vals, TAU * -0.25)],
//         ];
//         this.reset();
//     }
//     reset() {
//         this.history = [];
//         this.RNG.seed = 0;
//         this.import(`      
//         W,W,W,
//         W,W,W,
//         W,W,W,
//   O,O,O,G,G,G,R,R,R,B,B,B,
//   O,O,O,G,G,G,R,R,R,B,B,B,
//   O,O,O,G,G,G,R,R,R,B,B,B,
//         Y,Y,Y,
//         Y,Y,Y,
//         Y,Y,Y`);
//     }
//     copy() {
//         return new Cube().import(this.export());
//     }
//     vector2action(vector) {
//         var entries = Object.entries(rotmap);
//         var i = findbestIndex(entries, ([key, value]) => {
//             return -vector.to(value).length();
//         });
//         return entries[i][0];
//     }
//     action2vector(action) {
//         return rotmap[action].c();
//     }
//     changePerspective(compositeActions, perspectives) {
//         var res = [];
//         for (var perspective of perspectives.split(/\s+/)) {
//             for (var compositeAction of compositeActions) {
//                 var rotatedCompositeAction = '';
//                 for (var action of compositeAction.split(/\s+/)) {
//                     var vector = this.action2vector(action);
//                     axisRotate(vector, actionrotate2frontmap[perspective], actionrotate2frontmap[perspective].length());
//                     rotatedCompositeAction += `${this.vector2action(vector)} `;
//                 }
//                 rotatedCompositeAction = rotatedCompositeAction.trim();
//                 res.push(rotatedCompositeAction);
//             }
//         }
//         return res;
//     }
//     //could also give higher level actions
//     generateGraph(actions) {
//         this.graph2d = [];
//         this.graph3d = [];
//         var tempcube = new Cube();
//         this.tempcube = tempcube;
//         //3d ------------------------------------------
//         for (var cubelet of tempcube.cubelets) {
//             this.graph3d.push(new Knot({
//                 pos: cubelet.startpos.c(),
//             }));
//         }
//         for (var action of actions) {
//             tempcube.reset();
//             tempcube.apply(action);
//             for (var cubelet of tempcube.cubelets) {
//                 //edges are only usefull if the action moves the cubelet
//                 if (cubelet.pos.equals(cubelet.startpos) == false) {
//                     var orginalknot = this.graph3d.find(k => k.pos.equals(cubelet.startpos));
//                     var newknot = this.graph3d.find(k => k.pos.equals(cubelet.pos));
//                     orginalknot.edges.push(new Edge({
//                         target: newknot,
//                         data: action,
//                         cost: action.split(/\s+/).length,
//                     }));
//                 }
//             }
//         }
//         //3d -------------------------------------------------
//         //2d ----------------------------------------------
//         for (var face of tempcube.cubeletFaces) {
//             var pos2d = face.getCurrentPosition2D(this);
//             this.graph2d.push(new Knot({
//                 pos: pos2d,
//             }));
//         }
//         for (var action of actions) {
//             tempcube.reset();
//             tempcube.apply(action);
//             for (var face of tempcube.cubeletFaces) {
//                 if (face.getCurrentPosition2D(this).equals(face.getStartPosition2D(this)) == false) {
//                     var originalknot = this.graph2d.find(k => k.pos.equals(face.getStartPosition2D(this)));
//                     var newknot = this.graph2d.find(k => k.pos.equals(face.getCurrentPosition2D(this)));
//                     originalknot.edges.push(new Edge({
//                         target: newknot,
//                         data: action,
//                         cost: action.split(/\s+/).length,
//                     }));
//                 }
//             }
//         }
//     }
//     pathfind2d(dest) {
//         var misplacedface = this.cubeletFaces.find(f => f.getStartPosition2D(this).equals(dest));
//         var start = this.graph2d.find(k => k.pos.equals(misplacedface.getCurrentPosition2D(this)));
//         var goal = this.graph2d.find(k => k.pos.equals(misplacedface.getStartPosition2D(this)));
//         return pathfind(start, goal, this.graph2d).map(e => e.data).join(' ');
//     }
//     pathfind3d(position) {
//         var misplacedpiece = this.cubelets.find(c => c.startpos.equals(position));
//         var start = this.graph3d.find(k => k.pos.equals(misplacedpiece.pos));
//         var dest = this.graph3d.find(k => k.pos.equals(misplacedpiece.startpos));
//         return pathfind(start, dest, this.graph3d).map(e => e.data).join(' ');
//     }
//     apply(rotations, savehistory = true, perspective = 'F') {
//         if (rotations) {
//             rotations = this.changePerspective([rotations], perspective)[0];
//             if (savehistory) {
//                 this.history = this.history.concat(rotations.split(/\s+/));
//             }
//             var rots = this.string2rots(rotations);
//             for (var rot of rots) {
//                 this.rot(rot.c().normalize(), rot.length());
//             }
//         }
//         return rotations;
//     }

//     string2rots(input) {
//         return input.split(/\s+/).map(op => rotmap[op]);
//     }
//     rot(faceNormal, turns) {
//         var cubelets = this.cubelets.filter(c => c.pos.c().normalize().dot(faceNormal) > 0.1);
//         for (var cubelet of cubelets) {
//             axisRotate(cubelet.pos, faceNormal, turns);
//             for (var cubeletface of cubelet.faces) {
//                 axisRotate(cubeletface.normal, faceNormal, turns);
//             }
//         }
//     }
//     convert3dto2d(pos3d, normal) {
//         var [valnormal, offset, quat] = this.directionsposmap.find(vals => vals[0].equals(normal));
//         var frontrotated = Vector.fromArray(quat.rotateVector(pos3d.c().vals)).round();
//         return new Vector(frontrotated.x + offset.x, frontrotated.y * -1 + offset.y);
//     }
//     convert2dto3d(pos) {
//         return null;
//     }
//     genrandomize(count) {
//         var rots = Object.keys(rotmap);
//         var res = '';
//         for (var i = 0; i < count; i++) {
//             res += rots[Math.floor(Math.random() * rots.length)];
//         }
//         return res;
//     }

//     //check pattern against 2dgrid
//     detect(pattern, center, rotations, output) {
//         var rows = pattern.split('-');
//         var grid = rows.map(r => r.trim().split(/\s+/));
//         var samplepoints = [
//             new Vector(-1, -1), new Vector(0, -1), new Vector(1, -1),
//             new Vector(-1, 0), new Vector(0, 0), new Vector(1, 0),
//             new Vector(-1, 1), new Vector(0, 1), new Vector(-1, 1)
//         ];
//         for (var i = 0; i < rotations.length; i++) {
//             var rotation = rotations[i];
//             var match = true;
//             for (var samplepoint of samplepoints) {
//                 var rotatedpoint = axisRotate(samplepoint.c(), new Vector(0, 0, 1), rotation).add(new Vector(1, 1));
//                 var patterncolor = grid[rotatedpoint.y][rotatedpoint.x];
//                 var face = this.getFace(samplepoint.c().add(center));
//                 if (patterncolor != 'X' && face.color[0].toUpperCase() != patterncolor) {
//                     match = false;
//                     break;
//                 }
//             }
//             if (match) {
//                 output.push(i);
//             }
//         }
//         return output.length > 0;
//     }
//     getFace(position) {
//         return this.cubeletFaces.find(f => f.getCurrentPosition2D(this).equals(position));
//     }
//     scramble() {
//         rngseedelement.valueAsNumber = this.RNG.seed;
//         var options = ['F', 'R', 'U', 'L', 'D', 'B'];
//         var actions = '';
//         for (var i = 0; i < 20; i++) {
//             actions += `${options[Math.floor(this.RNG.range(0, options.length))]} `;
//         }
//         actions = actions.trim();
//         return actions;
//     }

//     import(data) {
//         var colorsgrid = data.trim().split('\n').map(row => row.split(',').filter((cell) => cell != false).map(cell => cell.trim()));
//         for (var i of [0, 1, 2, 6, 7, 8]) {
//             colorsgrid[i].splice(0, 0, null, null, null);
//         }
//         this.cubelets = [];
//         this.cubeletFaces = [];
//         for (var x = -1; x < 2; x++) {
//             for (var y = -1; y < 2; y++) {
//                 for (var z = -1; z < 2; z++) {
//                     var normals = [];
//                     if (x != 0) {
//                         normals.push(new Vector(x, 0, 0));
//                     }
//                     if (y != 0) {
//                         normals.push(new Vector(0, y, 0));
//                     }
//                     if (z != 0) {
//                         normals.push(new Vector(0, 0, z));
//                     }
//                     var cubelet = new CubeLet({
//                         pos: new Vector(x, y, z),
//                         startpos: new Vector(0, 0, 0),
//                         type: {
//                             0: 'core',
//                             1: 'center',
//                             2: 'edge',
//                             3: 'corner',
//                         }[normals.length],
//                     });
//                     this.cubelets.push(cubelet);
//                     for (var normal of normals) {
//                         var vec2d = this.convert3dto2d(new Vector(x, y, z), normal);
//                         var colorabrrev = colorsgrid[vec2d.y][vec2d.x];
//                         var startnormal = color2normalmap[colorabrrev];
//                         for (var i = 0; i < 3; i++) {
//                             if (startnormal.vals[i] != 0) {
//                                 cubelet.startpos.vals[i] = startnormal.vals[i];
//                             }
//                         }
//                         var newface = new CubeLetFace({
//                             color: abbrevcolor2colormap[colorabrrev],
//                             parent: cubelet,
//                             normal: normal,
//                             startnormal: startnormal,
//                         });
//                         cubelet.faces.push(newface);
//                         this.cubeletFaces.push(newface);
//                     }
//                 }
//             }
//         }
//         return this;
//     }
//     detectErrors() {
//         var combis = {};
//         var errors = [];
//         for (var cubelet of this.cubelets) {
//             var sp = vec2string(cubelet.startpos);
//             if (sp in combis) {
//                 var colorsofcubelet = cubelet.faces.map(f => f.color).join(',');
//                 errors.push(`duplicate piece (${colorsofcubelet}) pos:${vec2string(combis[sp])} pos2: ${vec2string(cubelet.pos)}`);
//             }
//             combis[sp] = cubelet.pos;
//         }
//         return errors;
//     }
// }
// function vectorequals(a, b) {
//     return a.x == b.x && a.y == b.y && a.z == b.z;
// }
// function isSameDirection(a, b, slag) {
//     return a.c().normalize().dot(b) > slag;
// }
// function axisRotate(v, axis, turns) {
//     var added = false;
//     if (v.vals.length == 2) {
//         v.vals.push(0);
//         added = true;
//     }
//     var quat = Quaternion.fromAxisAngle(axis.vals, turns * TAU);
//     v.vals = quat.rotateVector(v.vals);
//     if (added) {
//         v.vals.splice(v.vals.length - 1, 1);
//     }
//     v.round();
//     return v;
// }
// function vec2string(v) {
//     return v.vals.join(',');
// }
// class Knot {
//     constructor(obj) {
//         this.edges = [];
//         Object.assign(this, obj);
//     }
// }
// class Edge {
//     constructor(obj) {
//         Object.assign(this, obj);
//     }
// }
// function pathfind(start, dest, graph) {
//     for (var knot of graph) {
//         knot.cost = Number.MAX_VALUE;
//         knot.predecessor = null;
//     }
//     start.cost = 0;
//     var explored = [];
//     var frontier = [start];
//     while (frontier.length > 0) {
//         var smallest = 0;
//         for (var i = 1; i < frontier.length; i++) {
//             if (frontier[i].cost < frontier[smallest].cost) {
//                 smallest = i;
//             }
//         }
//         var current = frontier.splice(smallest, 1)[0];
//         if (current == dest) {
//             break;
//         }
//         for (var edge of current.edges) {
//             if (current.cost + edge.cost < edge.target.cost) {
//                 edge.target.predecessor = current;
//                 edge.target.usedEdge = edge;
//                 edge.target.cost = current.cost + edge.cost;
//                 frontier.push(edge.target);
//             }
//         }
//         explored.push(current);
//     }
//     return traceback(start, dest);
// }
// function traceback(start, destination) {
//     var res = [];
//     var current = destination;
//     while (current != start && current != null) {
//         res.push(current.usedEdge);
//         current = current.predecessor;
//     }
//     return res.reverse();
// }
// /// <reference path="libs/vector/vector.ts" />
// /// <reference path="libs/utils/rng.ts" />
// /// <reference path="libs/utils/store.ts" />
// /// <reference path="libs/utils/table.ts" />
// /// <reference path="libs/utils/utils.ts" />
// /// <reference path="libs/utils/stopwatch.ts" />
// /// <reference path="libs/utils/ability.ts" />
// /// <reference path="libs/utils/anim.ts" />
// /// <reference path="libs/rect/rect.ts" />
// /// <reference path="libs/event/eventqueue.ts" />
// /// <reference path="libs/event/eventsystem.ts" />
// /// <reference path="libs/utils/camera.ts" />
// /// <reference path="libs/networking/entity.ts" />
// /// <reference path="libs/networking/server.ts" />
// /// <reference path="cube.ts" />
// /// <reference path="pathfind.ts" />

// var gridsize = 50;
// var screensize = new Vector(1000, 500);
// var { canvas, ctxt } = createCanvas(screensize.x, screensize.y);
// var cube = new Cube();
// var rngseedelement = document.querySelector('#seedvalue');
// var erroroutput = document.querySelector('#erroroutput');
// cube.RNG.seed = rngseedelement.valueAsNumber;
// rngseedelement.addEventListener('change', e => {
//     cube.RNG.seed = rngseedelement.valueAsNumber;
// });



// function createButton(name, callback) {
//     var specialbuttoncontainer = document.querySelector('#specialbtncontainer');
//     specialbuttoncontainer.insertAdjacentHTML('beforeend', `<button>${name}</button>`);
//     specialbuttoncontainer.lastElementChild.addEventListener('click', callback);
// }
// var scramble = document.querySelector('#scramble');
// createButton('Reset', e => cube.reset());
// createButton('Scramble', e => scramble.value = cube.scramble());

// createButton('Apply', (e) => {
//     cube.apply(scramble.value, true, perspectiveSelect.value);
//     if (e.ctrlKey == false) {
//     }
// });
// createButton('Apply1', e => {
//     cube.apply(take1fromscramble(), true, perspectiveSelect.value);
// });



// createButton('import', e => { cube.import(scramble.value); });
// document.addEventListener('keydown', e => {
//     var keymap = {
//         'KeyU': 'U',
//         'KeyF': 'F',
//         'KeyD': 'D',
//         'KeyL': 'L',
//         'KeyB': 'B',
//         'KeyR': 'R',black
        
//     };
//     if (keymap[e.code] && document.activeElement != scramble) {
//         cube.apply(keymap[e.code], true, perspectiveSelect.value);
//     }
// });
// loop((dt) => {
//     ctxt.fillStyle = 'black';
//     ctxt.fillRect(0, 0, screensize.x, screensize.y);
//     drawCube(cube, ctxt);
// });
// function drawCube(cube, ctxt) {
//     for (var face of cube.cubeletFaces) {
//         var pos2d = cube.convert3dto2d(face.parent.pos, face.normal);
//         var abs = pos2d.c().scale(gridsize);
//         ctxt.fillStyle = face.color;
//         ctxt.fillRect(abs.x, abs.y, gridsize, gridsize);

//     }
// }
// function take1fromscramble() {
//     var index = scramble.value.search(/\s+/);
//     var out = scramble.value.substr(0, index);
//     scramble.value = scramble.value.substr(index).trim();
//     return out;
// }
