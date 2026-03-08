from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import String,Integer,Boolean,Float,Date
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from datetime import date
from typing import List, Optional

#la classe de base dont tous les modèles hériteront 
class Base(DeclarativeBase):
    pass


#Utilisateur
class Utilisateur(Base):
    __tablename__="utilisateur"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(100),unique=True)
    mot_de_passe: Mapped[str] =mapped_column(String(255))
    prenom: Mapped[str] = mapped_column(String(100))
    nom: Mapped[str] = mapped_column(String(100))
    mobile: Mapped[str] = mapped_column(String(20))
    role: Mapped[str] = mapped_column(String(50))
    date_creation: Mapped[date] = mapped_column(Date)
    actif: Mapped[Boolean] = mapped_column(Boolean)


    utilisateur = relationship("Utilisateur")


    def __repr__(self) -> str:
        return (
            f"Utilisateur(id={self.id!r}, email={self.email!r},"
            f"prenom={self.prenom!r}, nom={self.nom!r},"
            f"nom={self.mobile!r}, role={self.role!r},"
            f"date_creation={self.date_creation}, actif={self.actif!r},)"
        )
    

 
#Adresse
class Adresse(Base):
    __tablename__="adresse"
    id: Mapped[int] = mapped_column(primary_key=True)
    utilisateur_id: Mapped[int] = mapped_column(ForeignKey("utilisateur.id"))
    rue: Mapped[str] = mapped_column(String(255))
    ville: Mapped[str] = mapped_column(String(100))
    code_postal: Mapped[str] = mapped_column(String(20))
    pays: Mapped[str] = mapped_column(String(100))

    adresses = relationship("Adresse", back_populates="utilisateur")
    

    def __repr__(self) -> str:
        return(
        
            f"Adresse(id={self.id!r}, utilisateur_id={self.utilisateur_id!r},"
            f"rue={self.rue!r}, ville={self.ville!r},"
            f"code_postal={self.code_postal!r}, pays={self.pays!r})"
        )



#produit
class Produit(Base):
    __tablename__="produit"
    id: Mapped[int] = mapped_column(primary_key=True)
    id_modele: Mapped[int] = mapped_column(ForeignKey("modele.id"))
    lmei: Mapped[str] = mapped_column(String(20),unique=True)
    stockage: Mapped[int] = mapped_column(Integer)
    couleur: Mapped[str] = mapped_column(String(20))
    prix: Mapped[float] = mapped_column(Float)
    prix_de_vente: Mapped[float] = mapped_column(Float)
    annee_de_sortie: Mapped[int] = mapped_column(Integer)
    numero_de_garantie: Mapped[str] = mapped_column(String(100))
    statut: Mapped[str] = mapped_column(String(20))

    modele: Mapped["Modele"] = relationship(back_populates="produits")


    def __repr__(self) -> str:
        return(
        
            f"Produit(id={self.id!r}, id_modele={self.id_modele!r},"
            f"imei={self.imei!r}, stockage={self.stockage!r},"
            f"couleur={self.couleur!r}, prix={self.prix!r},"
            f"prix_de_vente={self.prix_de_vente!r}, annee_de_sortie={self.annee_de_sortie!r},"
            f"numero_de_garantie={self.numero_de_garantie!r}, statut={self.statut!r})"
        )



#Modeles
class Modele(Base):
    __tablename__="modele"
    id: Mapped[int] = mapped_column(primary_key=True)
    marque_id: Mapped[int] = mapped_column(ForeignKey("marque.id"))
    modele: Mapped[str] = mapped_column(String(100))
    date_de_sortie: Mapped[date] = mapped_column(Date)
    taille_ecran: Mapped[float] = mapped_column(Float)
    capacite_batterie: Mapped[int] = mapped_column(Integer)

    produits: Mapped[List["Produit"]] = relationship(back_populates="modele")
    marque: Mapped["Marque"] = relationship(back_populates="modeles")


    def __repr__(self) -> str:
        return(
        
            f"Modele(id={self.id!r}, marque_id={self.marque_id!r},"
            f"modele={self.modele!r}, date_de_sortie={self.date_de_sortie!r},"
            f"taille_ecran={self.taille_ecran!r}, capacite_batterie={self.capacite_batterie!r})"
        )


#marque
class Marque(Base):
    __tablename__="marque"
    id: Mapped[int] = mapped_column(primary_key=True)
    marque: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return(
        
            f"Modele(id={self.id!r}, marque={self.marque!r})"

        )
    
#Commandes 
class Commandes(Base):
    __tablename__="commandes"
    id: Mapped[int] = mapped_column(primary_key=True)
    utilisateur_id: Mapped[int] = mapped_column(ForeignKey("utilisateur.id"))
    statut: Mapped[str] = mapped_column(String(30))
    prix_total: Mapped[float] = mapped_column(Float)
    adresse_livraison: Mapped[str] = mapped_column(String(255))
    date_de_commande: Mapped[date] = mapped_column(Date)

    articles: Mapped[list["Article"]] = relationship(back_populates="commande")


    def __repr__(self) -> str:
        return(
        
            f"Commandes(id={self.id!r}, utilisateur_id={self.utilisateur_id!r},"
            f"statut={self.statut!r}, prix_total={self.prix_total!r},"
            f"adresse_livraison={self.adresse_livraison!r}, date_de_commande={self.date_de_commande!r})"
        )

#Articles commandés 
class Article(Base):
    __tablename__="article"
    id: Mapped[int] = mapped_column(primary_key=True)
    commande_id: Mapped[int] = mapped_column(ForeignKey("commandes.id"))
    produit_id: Mapped[int] = mapped_column(ForeignKey("produit.id"))
    prix: Mapped[float] = mapped_column(Float) 
    quantite: Mapped[int] = mapped_column(Integer)

    commande: Mapped["Commandes"] = relationship(back_populates="articles")


    def __repr__(self) -> str:
        return(
        
            f"Article(id={self.id!r}, commande_id={self.commande_id!r},"
            f"produit_id={self.produit_id!r}, prix={self.prix!r},"
            f"quantite={self.quantite!r})"
        )
    


#livraison 
class Livraison(Base):
    __tablename__="livraison"
    id: Mapped[int] = mapped_column(primary_key=True)
    commande_id: Mapped[int] = mapped_column(ForeignKey("commandes.id"))
    service_livraison: Mapped[str] = mapped_column(String(255))
    numero_commande: Mapped[str] = mapped_column(String(100),unique=True)
    statut: Mapped[str] = mapped_column(String(30))
    date_expedition: Mapped[date] = mapped_column(Date)
    date_livraison: Mapped[date] = mapped_column(Date)

    commande = relationship("Commande", back_populates="livraison")

    def __repr__(self) -> str:
        return(
        
            f"Livraison(id={self.id!r}, commande_id={self.commande_id!r},"
            f"service_livraison={self.service_livraison!r}, numero_commande={self.numero_commande!r},"
            f"statut={self.statut!r}, date_expedition={self.date_expedition!r}, date_livraison={self.date_livraison!r}),"
        )


#paiement
class Paiement(Base):
    __tablename__="paiement"
    id: Mapped[int] = mapped_column(primary_key=True)
    commande_id: Mapped[int] = mapped_column(ForeignKey("commandes.id"))
    utilisateur_id: Mapped[int] = mapped_column(ForeignKey("utilisateur.id"))
    montant: Mapped[float] = mapped_column(Float)
    moyen_paiement: Mapped[str] = mapped_column(String(30))
    statut: Mapped[str] = mapped_column(String(30))
    reference: Mapped[str] = mapped_column(String(30),unique=True)
    date_paiement: Mapped[date] = mapped_column(Date)


    commande = relationship("Commande")
    utilisateur = relationship("Utilisateur")

    def __repr__(self) -> str:
        return(
        
            f"Paiement(id={self.id!r}, commande_id={self.commande_id!r},"
            f"utilisateur_id={self.utilisateur_id!r}, montant={self.montant!r},"
            f"moyen_paiement={self.moyen_paiement!r}, statut={self.statut!r}, reference={self.reference!r}, date_paiement={self.date_paiement!r})"
        )









