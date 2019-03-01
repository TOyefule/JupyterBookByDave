# Lesson 31 - Junit Test Suite

# Test suite

## Learning Objectives
      * Test suite to bundle few unit test cases and run them together

## The Walkthrough
  ---------------------------
  1. Create a Spring Boot Application
      * Name it SpringBoot13_unitTest
      * Add the dependencies for the web, jpa, h2 and thymeleaf
      * Hit next until you finish the wizard, and then wait until it's done.

  2. Create a Class
      * Right click on com.example.demo and click New -> Class
      * Name it Actor.java
      * Edit it to look like this:
    
```java
import javax.persistence.*;
import java.util.HashSet;
import java.util.Set;

@Entity
public class Actor {
  @Id
  @GeneratedValue(strategy = GenerationType.AUTO)
  private long id;
  private String name;
  private String realname;

  @ManyToMany(mappedBy = "cast")
  private Set<Movie> movies;


  public Actor() {
    Set<Movie> movies = new HashSet<>();
  }
  }
}
```
3. Auto generate getters and setters
    * Right click inside the Actor class and select
    generate -> Getters and Setters
  * Select all the fields listed and click ok

4. Create a Class
    * Right click on com.example.demo and click New -> Class
    * Name it Movie.java
    * Edit it to look like this:

```java
import javax.persistence.*;
import java.util.Set;

@Entity
public class Movie {
  @Id
  @GeneratedValue(strategy = GenerationType.AUTO)
  private long id;

  private String title;
  private long year;
  private String description;

  @ManyToMany
  private Set<Actor> cast;
  }
}
```  
5. Auto generate getters and setters
    * Right click inside the Movie class and select generate -> Getters
    and Setters
  * Select all the fields listed and click ok


6. Create a Repository
    * Right click on com.example.demo and click New -> Class
    * Change the value of the drop-down box to Interface
    * Name it ActorRepository.java
    * Edit it to look like this:

```java
import org.springframework.data.repository.CrudRepository;

public interface ActorRepository extends CrudRepository<Actor, Long>{
}
```

## Create unit tests

7. Create a Test Class
    * Click on test folder
    * Open java folder
    * Open com.example.demo
    * Right click on com.example.demo and create a class called TestFindById.java
    * Edit it to look like this:

```java
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.jdbc.AutoConfigureTestDatabase;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.test.context.junit4.SpringRunner;

import java.util.HashSet;
import java.util.Set;

import static org.junit.Assert.assertEquals;
@RunWith(SpringRunner.class)
@DataJpaTest
@AutoConfigureTestDatabase(replace=AutoConfigureTestDatabase.Replace.NONE)
public class TestFindById {

  @Autowired
  ActorRepository actorRepository;

  @Test
  public void findById() {
    Actor actor = new Actor();
    actor.setName("Sandra Bullock");
    actor.setRealname("Sandra Mae Bullowski");

    Movie movie = new Movie();
    movie.setTitle("Emoji Movie");
    movie.setYear(2017);
    movie.setDescription("About Emojis...");

    Set<Movie> movies = new HashSet<Movie>();
    movies.add(movie);

    actor.setMovies(movies);
    actorRepository.save(actor);
    assertEquals(actorRepository.findById(1L).get().getId(), actor.getId());
  }
}
```

8. Create a Test Class
    * Click on test folder
    * Open java folder
    * Open com.example.demo
    * Right click on com.example.demo and create a class called TestFindByName.java
    * Edit it to look like this:

```java    
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.jdbc.AutoConfigureTestDatabase;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.test.context.junit4.SpringRunner;

import java.util.HashSet;
import java.util.Set;

import static org.junit.Assert.assertEquals;
@RunWith(SpringRunner.class)
@DataJpaTest
@AutoConfigureTestDatabase(replace=AutoConfigureTestDatabase.Replace.NONE)
public class TestFindByName {

  @Autowired
  ActorRepository actorRepository;

  @Test
  public void findByName() {
    Actor actor1 = new Actor();
    actor1.setName("David Bullock");
    actor1.setRealname("David Mae Bullowski");

    Movie movie1 = new Movie();
    movie1.setTitle("Some Movie");
    movie1.setYear(2019);
    movie1.setDescription("About some movie...");

    Set<Movie> movies1 = new HashSet<Movie>();
    movies1.add(movie1);

    actor1.setMovies(movies1);
    actorRepository.save(actor1);

    assertEquals(actorRepository.findByName("David Bullock").getName(), "David " +
            "Bullock");
  }
}
```

9. Create a Test Class
    * Click on test folder
    * Open java folder
    * Open com.example.demo
    * ight click on com.example.demo and create a class called TestFindAllActors.java
    * Edit it to look like this:

```java    
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.jdbc.AutoConfigureTestDatabase;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.test.context.junit4.SpringRunner;

import java.util.HashSet;
import java.util.Set;

import static org.junit.Assert.assertEquals;
@RunWith(SpringRunner.class)
@DataJpaTest
@AutoConfigureTestDatabase(replace=AutoConfigureTestDatabase.Replace.NONE)
public class TestFindAllActors {

  @Autowired
  ActorRepository actorRepository;

 @Test
  public void findAllActors() {
    Actor actor2 = new Actor();
    actor2.setName("David Bullock");
    actor2.setRealname("David Mae Bullowski");

    Movie movie2 = new Movie();
    movie2.setTitle("Some Movie");
    movie2.setYear(2019);
    movie2.setDescription("About some movie...");

    Set<Movie> movies2 = new HashSet<Movie>();
    movies2.add(movie2);

    actor2.setMovies(movies2);
    actorRepository.save(actor2);

    assertEquals(actorRepository.findAllById(3L).getId(), actor2.getId());
  }
}
```

10. Create a Test Suite Class
    * Click on test folder
    * Open java folder
    * Open com.example.demo
    * Right click on com.example.demo and create a class called TestSuite.java
    * Edit it to look like this:

```java
import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import org.springframework.boot.test.context.SpringBootTest;

@RunWith(Suite.class)

@Suite.SuiteClasses({
        TestFindById.class,
        TestFindByName.class,
        TestfindAllActors.class
})

@SpringBootTest
public class TestSuite {

}
```

11. Run your test TestSuite
Right click on the TestSuite class and run TestSuite. After you run a test,
the Run tool window will display the test runner tab with the results of
your testing session.

## What is Going On
Test suite is used to bundle a few unit test cases and run them together. In
this lesson MovieTest1 and MovieTest2 are run together using the Test Suite.
