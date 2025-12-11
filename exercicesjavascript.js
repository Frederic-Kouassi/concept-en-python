
class Animal {
    constructor(nom, type, bruit) {
        this.nom = nom;     
        this.type = type;
        this.bruit = bruit;
    }

    faireBruit() {
        return `${this.nom} (${this.type}) fait : ${this.bruit}`;
    }
}


class Lion extends Animal {
    constructor(nom) {
        super(nom, "Lion", "Roooaaar !");
    }

    faireBruit() {
        return `Le lion ${this.nom} rougit: ${this.bruit}`;
    }
}


class Elephant extends Animal {
    constructor(nom) {
        super(nom, "Éléphant", "Prrrrr !");
    }

    faireBruit() {
        return `L'éléphant ${this.nom} barrit : ${this.bruit}`;
    }
}


class Zoo {
    constructor() {
        this.animaux = [];
    }

    ajouterAnimal(animal) {
        this.animaux.push(animal);
    }

    afficherTousLesBruits() {
        this.animaux.forEach(animal => {
            console.log(animal.faireBruit());
        });
    }
}


const zoo = new Zoo();
zoo.ajouterAnimal(new Lion("Simba"));
zoo.ajouterAnimal(new Elephant("Dumbo"));
zoo.ajouterAnimal(new Lion("Golo"));
zoo.ajouterAnimal(new Elephant("dodo"));

zoo.afficherTousLesBruits();
