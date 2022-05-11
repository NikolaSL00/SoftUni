import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;

public class Main {

    public static void main(String[] args) {
        EntityManagerFactory factory =
                Persistence.createEntityManagerFactory("CodeFirstEx");

        EntityManager entityManager = factory.createEntityManager();

        entityManager.getTransaction().begin();

        User user = new User("marina", AccountType.GOLD);
        entityManager.persist(user);

        entityManager.getTransaction().commit();
        entityManager.close();
    }
}
