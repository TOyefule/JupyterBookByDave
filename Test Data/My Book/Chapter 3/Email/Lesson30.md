# Lesson 30 - Junit Unit Test

# Unit Test

## The Walkthrough
---------------------------
1. Create a Spring Boot Application
  * Name it SpringBoot_10_unitTest
  * Add the dependencies for the web, thymeleaf, jpa and h2
  * Hit next until you finish the wizard, and then wait until it's done.

2. Create a Class
  * Right click on com.example.demo and click New -> Class
  * Name it Course.java
  * Edit it to look like this:
```java
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.validation.constraints.Min;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;

@Entity
public class Course {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private long id;

    @NotNull
    @Size(min=4)
    private String title;

    @NotNull
    @Size(min=3)
    private String instructor;

    @NotNull
    @Size(min=10)
    private String description;

    @NotNull
    @Min(3)
    private int credit;
}
```

3. Auto generate getters and setters
    * Right click on the word Course in the class declaration and select
    generate -> Getters and Setters
  * Select all the fields listed and click ok

4. Create a Class
  * Click on test
  * Open java folder
  * Open com.example.demo
  * Open Tests.java
  * Edit it to look like this:

```java
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

import java.util.EmptyStackException;
import java.util.Optional;

import static org.junit.Assert.assertEquals;

@RunWith(SpringRunner.class)
@SpringBootTest
public class Tests {

  @Autowired
  CourseRepository courseRepository;

  @Test
  public void updateCourse() {
    Course course2 = new Course();
    course2.setTitle("Math102");
    course2.setInstructor("Dave Hills");
    course2.setDescription("Here is the description");
    course2.setCredit(3);
    courseRepository.save(course2);
    assertEquals(courseRepository.findAllById(1L).getId(), course2.getId());
  }

  @Test
  public void deleteCourse() {
    Course course3 = new Course();
    course3.setTitle("Math103");
    course3.setInstructor("Chi Hills");
    course3.setDescription("Here is the description");
    course3.setCredit(3);
    courseRepository.save(course3);
    courseRepository.deleteById(1L);
    assertEquals(courseRepository.findById(1L), Optional.empty());
  }

  @Test
  public void findCourse() {
    Course course1 = new Course();
    course1.setId(3);
    course1.setTitle("Math101");
    course1.setInstructor("Fi Hills");
    course1.setDescription("Here is the description");
    course1.setCredit(4);
    courseRepository.save(course1);
    assertEquals(courseRepository.findById(3L).get().getTitle()
            , "Math101");
  }
}
```

5. Run your test TestSuite
Right click on the Test class and run Tests. After you run the test, 
the Run tool window will display the test runner tab with the results of
your testing session.

## What is Going On
Unit testing is breaking down the program into smaller junks of code to
perform a serious of tests.
JUnit is a testing framework for Java programming language. Junit gives you support for 
writing unit tests more easily. 
@Test annotation is used to mark that a method is a test method. 
assertEquals() checks that the two objects are equal or not. 
JUnit library needs to imported to use the @Test and assertTrue methods. 


