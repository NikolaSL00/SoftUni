import entities.Town;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;
import javax.persistence.Query;
import java.util.List;

public class _02_ChangeCasing {

    public static void main(String[] args){

        // JPA interface implemented

        EntityManagerFactory factory =
                Persistence.createEntityManagerFactory("PU_Name");

        EntityManager entityManager = factory.createEntityManager();

        try{
            entityManager.getTransaction().begin();

            // entityManager.createQuery("UPDATE Town t SET t.name = lower(t.name) " + "WHERE length(t.name) >= 5");
            Query from_town = entityManager
                    .createQuery("Select t From Town t", Town.class);

            List<Town> listResult = from_town.getResultList();

            for (Town town : listResult) {
                String name = town.getName();
                if(name.length() <= 5){
                    String nameToUpper = name.toUpperCase();
                    town.setName(nameToUpper);

                    entityManager.persist(town);
                }
            }
            entityManager.getTransaction().commit();
        } catch (Exception e) {
            entityManager.getTransaction().rollback();
        }
        entityManager.close();

    }
}
