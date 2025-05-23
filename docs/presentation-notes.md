# Presentation Notes 
## Unit Testing and TDD - Python 

This workshop is a basic, hands-on introduction to fundamental unit testing concepts and practices. This version of the workshop uses Python for the hands-on work.

The introduction is broad rather than deep - we'll touch on three kinds of executable tests that typically exercise code at the "unit" level, including example-based testing, property-based testing, and mutation testing. 

We'll practice writing unit tests for existing code, writing unit tests as executable specifications to drive out new code, and refactoring existing code and using mocks to enable isolated unit testing. We'll demonstrate property-based tests and mutation tests. We will not go into great depth in any of these topics. 

We'll clarify some terminology about testing that often causes confusion, as some terms are overloaded - that is, they have different meanings in different contexts. 

## Testing vs. Checking 

There are several ways to exercise software to discover what it does and verify whether it behaves as we want it to. People tend to refer to all the various activities as "testing," in a blanket way. It's unlikely this verbal habit will change. 

Yet, it's useful to keep in mind the distinction between repeatable, predictable activities and activities that require human creativity. Many professional software testers refer to the former as _checking_ the software, and reserve the word _testing_ for activities that require human creativity.

When we _check_ a software product, we're validating that it behaves as expected under controlled operating conditions and with predefined inputs. It's often feasible to automate software checks.

When we _test_ a software product, we're exploring its behavior to discover things about it that we don't already know, or for which we don't have predefined expectations to check against.

Unit testing is really a form of _checking_ software. It can be automated and included in a continuous integration / continuous delivery pipeline. 

## System Under Test (SUT) or Code Under Test (CUT) 

When we _test_ software we're usually working with the entire application. When we _check_ software we often exercise a subset of the application. We control the scope, the configuration, the execution environment, and the inputs passed to the portion of the application we're interested in checking. 

## Example-Based Testing 

Most of the executable test cases you will see and write are _example-based_ tests. Really, they are _checks_, but people say _tests_ anyway. Each case is an example of a _single interaction_ with a subset of the SUT. The entire _suite_ of tests may exercise the system pretty comprehensively. 

An example-based test case can exercise any subset of the SUT, large or small. Although there is no standard definition of a "unit" of software, when we write _unit tests_ we are usually trying to exercise the smallest subset of the SUT that can be run in isolation from the rest of the system. 

Just how small that is will depend on the characteristics of the programming language we're using. For Python, a unit test exercises one logical path through one method. 

## A check or test case or example 

With example-based testing, a single test case may be called a _test case_, an _example_, or a _check_. The most common term is _test case_.

## Test Automation 

Test automation is the practice of writing executable code that exercises the SUT, and setting it up to run automatically when a triggering event occurs. Typically, the triggering event is a commit to version control, which initiates the CI/CD pipeline. Automated checks are executed at various points in the pipeline to verify application behavior at different scopes. 

## A check can be automated if... 

People are often pretty casual about how they use the term _test automation_. Usually, all they mean is that the test cases are executable. That's fine for casual discussion, but there's more to test automation than that. 

In addition to being executable, the test case must not require any human intervention. If you have a script that prompts you for a userid or an IP address, that script can't be automated as-is. You'd have to modify it so that it provides any required inputs without human intervention. 

The test case also has to be _repeatable_. In the context of test automation, _repeatable_ means that every execution of the test case is identical. If you have to reset anything, change configuration settings, reload a database, or change input data between runs, then the test script is not repeatable. 

Finally, to be automated the test script has to start whenever appropriate without human intervention. Typically, the event that triggers execution is a commit to version control, and the thing that gets started is a CI/CD pipeline that includes any automated steps necessary to achieve the goal of the pipeline. This may include tests or checks, but also other things such as static code analysis, security scans, license checks, compiling source code, spinning up server instances, logging information for IT audits, and moving code between execution environments.

## Regression 

According to the American Heritage Dictionary, 5th edition, _to regress_ means "to return to a previous, usually worse or less developed state." 

People often say they want to "run regressions" or "do regressions" on a software product. I suspect that isn't quite what they really want to do. It's more likely that they want to _detect_ regressions before they find their way into production. 

_Regression tests_ help us do that. The _regressions_ as such are not what we want. 

## Regression Tests

Regression tests are _checks_. They compare the present behavior of the application with its previous (good) behavior. As such, they can usually be automated. Regression tests can be written at any level of abstraction, including the unit level. 

One benefit of having a comprehensive suite of unit tests is that they help us identify regressions early in the development process.

## What's a "unit?" 

_group discussion_ 

A source of confusion about unit testing is the fact there's no generally-accepted or standard definition of "software unit." Let participants discuss this and see if different opinions emerge. Guide them toward the understanding that we usually think of a software unit as _small_.  

## Scope (and cost) of a check or test 

To check application functionality end-to-end may require considerable setup time, the check is susceptible to failure for a variety of reasons besides the functionality of the SUT, execution time may be long, and there may not be enough time available to exercise the application sufficiently - we may have to skip some of the checks. Yet it is important to check the entire application to a reasonable extent.

When we check functionality at a fine-grained level, we can fully control the runtime conditions, configuration, and input data for the SUT. These checks are small, fast, cheap to run, and easy to modify, but each individual check exercises only a very small part of the application. 

What we'd like to have is the appropriate mix of fine-grained, mid-level, and end-to-end checks to give us high confidence in the code and to detect regressions accurately and early.

## Test Automation Pyramid 

The original test automation pyramid was built by the ancient Egyptians with the assistance of space aliens. Or not.

## It's a Triangle 

The test automation pyramid is really just a triangle. But pyramids are more impressive than triangles, so people like to call it a pyramid. No one visits Egypt to look at triangles.

## Many of these

The shape is meant to suggest that we want to write more fine-grained checks than large-scope ones, because they're fast, cheap, and point directly to the problem when they fail, so we don't have to spend much time in analysis to diagnose the problem. 

We want to cover as much functionality as we can at this level, so that we won't have to check that functionality with more-expensive and harder-to-maintain checks at higher levels. 

## Fewer of these

But not everything can be checked adequately at a fine-grained level. As we write checks of increasing scope, we want to continue to follow the philosophy of checking as much functionality as possible as low as possible on the pyramid...or triangle.

## Very few of these 

Ultimately we may need very few checks of large scope, like end-to-end tests. 

## Manual testing 

"Real" testing can't be automated, but is still important. We'll talk about a technique called Exploratory Testing later. As information about the behavior of the application is discovered through testing, we can often capture it in the form of executable checks once we understand what to expect and how to set up the conditions for the behavior in a repeatable way. 

## Michael Feathers' rules for a unit test

If there's no standard definition for "unit" and no common understanding of the word "test," how can we define the characteristics of a "unit test?"

Michael Feathers, a well-respected software engineer and technical coach, came up with some rules of thumb for unit tests back in 2005. Many people in the industry still use this as the basic guideline for unit tests. 

The first three points are related to the fact we want the unit check to fail for one reason only - the actual behavior of the SUT does not match the expected behavior. We don't want it to fail because of a network timeout or incorrect data in a test database. That won't tell us anything useful about the state of the application. 

We also don't want the checks to depend on each other. The main reason is so we can run any one of them, or a subset that pertains to some particular aspect of the application, without having failures just because some other check wasn't executed first. 

Another reason is to enable us to run a large test suite on multiple threads or on multiple servers concurrently, in the interest of time. 

Finally, if we have to tweak the environment then the check is dependent on human intervention, and can't be automated. 

## Python Unit Testing 

Let's take a look at some code and see what unit checks, or unit tests, look like. You can fork and clone the repo shown on the slide and play with it to your heart's content. 

Under the source directory, take a look at the file named age.py. It contains a method named categorize_by_age that takes an integer representing a person's age in years and returns a string description of the age range within which the person's age falls. So, if we pass in an age of 32, we'll get a description of "Adult." 

How would we write unit checks or unit tests for this code? Under the tests directory, open file test underscore age dot py. 

Different unit test libraries, also called "frameworks," have different conventions for naming test methods and other details, but they generally perform the same functions. There will be a test runner that inspects the test code to locate and execute test cases. 

Here we're using a Python unit test library called pytest. The test runner for pytest looks for classes whose names begin with "test" underscore, and within those classes it looks for methods whose names begin with the text, "test", and runs them. It bypasses other methods. 

The method test_an_8_yo_is_a_child illustrates the Arrange, Act, Assert pattern. This is common to all kinds of executable checks. First we need to set the preconditions for the test case. That's the Arrange part. Next, we run the code under test. That's the Act part. Finally, we assert the expected postconditions for the test case. That's the Assert part. 

We don't normally include comments to mark the three parts of each test case. Method test_a_10_yo_is_an_adolescent shows the way methods like this usually look. 

But it's also common to compress everything into as few lines as possible, since we'll probably have a very large number of these methods. Method test_a_21_yo_is_an_adult to see how this style looks. 

Some general coding conventions are different between test code and production code. We don't usually write hard-coded literals in production code, but it's common to do so in test code because we want to see at a glance what values were input and what values are expected in each test case. 

We don't want to have to scroll up and down or look at a separate source file to find the values that were used in the test case, when we're trying to resolve a problem. It comes down to a difference in how we use test code, and how we organize production code for maintainability.

## Arrange-Act-Assert 

We've been referring to the the three-part pattern for test cases as Arrange-Act-Assert. The same pattern goes by other names, too. They all mean the same thing. 

## Preconditions-Action-Postconditions 

Another set of terms for the same thing.

## Prepare-Run-Expect 

Another set of terms for the same thing.

## Given-When-Then

Another set of terms for the same thing. This one is commonly used with a related approach called _Behavior-Driven Development_. It's the same idea - set up the preconditions, exercise the SUT, assert the desired or expected postconditions.

## Changing Existing Code and Tests 

Let's say we wanted to add logic to this application to recognize people between the ages of 13 and 17 as "teenagers". We'd have to make a couple of small changes to both the production code in file age dot py and test file test underscore age dot py. 

There are a couple of approaches to this. Traditionally, people would first make the changes to the production code and then add or modify the relevant test cases in the test code. Some people call this approach "test-after" development, because you write the test cases after you've modified the production code. 

A more contemporary approach is first to adjust the test cases to reflect the behavior we want to see. When we've verified that the new or modified test cases fail because we haven't changed the production code yet, and not for some silly reason like a compilation error, we modify the production code so that the new test cases as well as the rest of them pass. 

This approach is called Test-Driven Development, or TDD, because you use the failing test cases to guide or "drive" the necessary logic in the production code. 

So, we want to see the result "Adolescent" for ages between 10 and 12, and the result "Teenager" for ages between 13 and 17. 

Let's try the traditional "test-after" approach first. Make the changes to age dot py and then modify the test cases in test underscore age dot py. 

_let participants work - assist as needed - discuss outcomes and how it felt_ 

## Shift Left Testing 

A long time ago, people came to realize that delaying testing until late in the delivery process leads to all kinds of trouble. Problems were not detected until most of the project schedule was used up and most of the budget spent. 

People started talking about shifting testing left, meaning starting testing activities earlier in the delivery cycle. This is assuming we read from right to left, of course. 

Before long, some people were shifting testing - or some of it, anyway - so far to the left that it happened before coding. Since there was no code for the tests to test, this changed the dynamic of software development in some ways. 

## Python TDD

Okay, now revert your changes. Get the code back into the state is was in when you started. 

Let's make the same changes, but this time modify the test cases first. 

One thing about the TDD approach is that we don't make all the changes at once. First change the test cases that verify the "Adolescent" age range. When those cases fail for the right reason, modify the production code just enough to make them pass. Make sure all the other existing test cases pass, too. 

Now examine the test code and the production code to look for any opportunities to simplify the design. There probably won't be any such opportunities in this example, but it's a good idea to take a moment to look for opportunities anyway, rather than just assuming.

Now that the application behaves the way we want it to for "Adolescents," repeat the same steps to add logic for the new "Teenager" category. 

_let participants work - assist as needed - discuss differences in the 2 approaches_ 

## If we write tests before production code...

_discuss_ 

## Test-Driven Development Mechanics 

What did we just do with the age class? It turns out there's a method to the madness of TDD. Mechanically, it's a repeating three-step process. Of course, there's more to think about than just that, but those are the bare mechanics of it.

_discuss slide content_ 

## Reverse Polish Notation 

Let's try test driving a complete application from scratch.

_describe what RPN is if any of the participants is unsure about it._ 

## Test-Driving a Reverse Polish Notation Calculator 

_let participants work - assist as needed - debrief_ 

# Refactoring 

We spend far more time working with existing code bases than we do writing greenfield code. We did a little of that when we modified the age categorization application to support "Teenagers." 

But in real life it isn't usually as simple as that example. We often have to change the structure or internal design of the code in order to make the changes we need, and keep the code in a form that's reasonable for unit testing. 

There's a buzzword for changing the internal structure or design of code while keeping its behavior the same - _refactoring_. 

You'll hear people using the word "refactoring" as a synonym for "change" - any kind of change. But it specifically means changing only the internal structure or design of code without changing the behavior of the code. 

Isn't it risky to make changes to code that might accidentally change its behavior? Changing behavior is the same as breaking functionality, right? How can we feel confident that our refactorings don't break something? 

_let the group answer. desired answer is the unit test suite is our safety net for refactoring_ 

Refactoring code tends to involve the same changes over and over. Martin Fowler developed a catalog of common refactorings. Later, Joshua Kerievsky published a book on refactoring to patterns - that is, the Design Patterns described in the Gang of Four book long ago. 

IDEs and smart editors like VSCode include some built-in support for basic refactorings. 

_demonstrate how to find refactorings in the VSCode UI._ 

_for instance, you can highlight a block of conditional code and right-click it to get a list of built-in refactorings that make sense in that context_ 

_the rename refactoring is so common that it has its own entry on the context menu_ 

_note that with Copilot enabled, we can engage it to perform refactorings on the code, too_ 

## Approaching a Code Base That Lacks Unit Tests 

An all-too-common situation is that we must make changes to an existing code base that doesn't have any executable tests to provide a safety net. 

Once we have a few tests in place, it becomes easier to work with the code. But initially, it may not be clear how we can _begin_ to work with the code. 

## Resources for Working with Existing Codebases 

There are a lot of resources online and in print to help us with this problem. Here are a couple of the best ones. 

Michael Feathers' book is on a short list of programming books that stands the test of time, because it doesn't go out of date as technologies evolve. Besides that, it's useful for working with older codebases whose source code _hasn't_ actually evolved. 

Emily Bache based the Gilded Rose refactoring kata on previous work by Bobby Johnson, and expanded it into what has become the single most popular exercise for practicing refactoring techniques. We're going to do that exercise in a minute. 

## Techniques for Working with Existing Codebases 

People have had to work with existing codebases for as long as software has existed. Some have come up with practical techniques that help us get started with it. 

I think Michael Feathers is the person who coined the term "seams" to refer to places in monolithic code where there's an obvious place to separate out some of the logic - for some definition of "obvious." 

_show some of the code from Gilded Rose and show how the if/else blocks seem to suggest places where we could pull out chunks of code_ 

Another way to discover secrets about the behavior of monolithic legacy code is to introduce so-called _sensing variables_ and then write unit test cases that assert bogus values for the variable, in order to generate test failures. We can then see what the value of certain elements are at specific points in the complex logic. 

The sensing variables and the test cases for them will not remain in the code, of course. They're temporary tools to help us understand what the code is doing. 

_demonstrate adding a sensing variable and writing a unit test cases for it - then delete that code_

In the YouTube video linked on the slide, Sandi Metz walks through the Gilded Rose refactoring kata using Ruby and demonstrates a technique she called the _squint test_. It means we can get some clues about how to restructure the code by paying attention to the visual shape of the source code as well as the color highlighting provided by our editor. 

The problematic code in the Gilded Rose exercise has a zig-zag shape due to the repetitious if/else blocks. This gives us some clues about where we might break up the code or add sensing variables to explore the behavior of the code. 

The boundaries of if/else blocks are often _seams_ where we can extract chunks of code into smaller methods. Once we've learned what the code is doing, we don't necessarily keep all those smaller methods. Method extraction may be one step in a longer process of understanding and remediating the code. 

When refactorings appear to be feasible, one approach is to go ahead and do them even while reading through the code for the first time. Arlo Belshee calls it _read by refactoring_. You don't just _look_ at the code, you go ahead and rip it apart as you go. In some cases this can help you understand what's going on in a big chunk of monolithic code.

_extract one or two chunks of if/else code to demonstrate the technique - then revert_ 

If you'd rather not risk confusing yourself by making the code even harder to understand, you can leave it as-is and write an _approval test_ for it. An approval test is not a unit check. It's a higher-level test that captures output from the SUT, usually in a file. 

Going forward, as we work with the legacy code we can periodically run the approval test to see if we've changed the application's behavior. The approval test doesn't tell us whether the code is correct, but it does signal us when we inadvertently change its behavior. 

The captured output file is called the _golden master_. We can compare the output from the application against the golden master at any time while working with the legacy code to see if we've inadvertently broken any logic. 

_run the provided test to produce a golden master - no need to remove this unless you want to_

Another way to provide a sort of safety net for modifying the legacy code is to introduce an abstraction layer between client code and the legacy application. That way, you can gradually change the underlying legacy code without affecting the client code. 

In a minute you'll see that the rules for the Gilded Rose kata prohibit us from touching the Item class. When you examine the code, you'll quickly realize the bad design stems from the Item class. If we could refactor it, the code for the updateQuality method could be much simpler and clearer.

In a situation like this, we can borrow a page from the _strangler_ pattern for gradually replacing an old implementation with a new one. That is, we can add an abstraction layer between the Item class and the updateQuality method. We can modify updateQuality to refer to an Item wrapper instance, and handle the peculiarities of the Item class there instead of all over the place in updateQuality.

## The Gilded Rose Refactoring Kata 

So we have some ideas for addressing the legacy code provided in the Gilded Rose exercise. There's no right or wrong way to approach it. 

_walk through the instructions and code and let the participants work on it_ 

## Using an LLM assistant 

VSCode comes bundled with Copilot, which is a controller for "any" coding LLM, for some definition of "any." 

Let's use Copilot to test-drive an implementation of a name formatter. 

_demonstrate the process of defining the name formatter via copilot for English names_ 

## Modifying Existing Code Using an LLM assistant 

Now it's your turn. Your task is to enhance the solution to support Spanish names. Spanish names have a different format from English names. 

A full Spanish name consists of the primer nombre, segundo nombre, primer appellido, and segundo appellido. Sometimes people omit the segundo nombre and/or segundo appellido when they provide their names on forms. 

It's a common convention to write the name as primer nombre, initial of the segundo nombre, primer appellido, and initial of the segundo appellido. 

Use Copilot to enhance the previous solution per the instructions on the slide. 

## Continuous Delivery Pipeline 

Unit tests fit into a CI/CD pipeline near the beginning, after any forms of static analysis that might be part of the pipeline and before any executable tests of greater scope than a "unit." 

## Checkpoint 

Here's what you've learned so far. 

## Other Kinds of Checking/Testing 

So far, everything we've covered falls under the heading of _example-based tests_. Each test case is an example of a single interaction with the SUT. 

Of course, we need to run executable checks and perform creative testing activities on larger subsets of the solution than individual units of code. That's what the test automation pyramid illustrates. 

But there's more we can do at the unit level. 

### Property-Based Testing 

There's a kind of executable check or test called a _property-based test_. Property-based tests compare the behavior of the SUT with a definition of the characteristics, or properties, of the code, treated as invariants. 

A PBT tool works by generating a massive number of inputs to the SUT and comparing the outputs to invariants. For instance, if the SUT has an integer argument, the tool will generate a test case for every possible integer value. 

During each run, the tool narrows down the number of test cases necessary to exercise the code fully, until we have just enough. That way, we aren't running millions or billions of tests that only repeat the same results. 

A PBT tool can almost always discover edge cases we didn't think of when we wrote our example-based tests. 

Take a look at the file named test underscore rpn underscore props dot py in directory property underscore tests. 

PBT tools for some languages can be pretty complicated to use. Fortunately, pytest supports PBT in a relatively straightforward way. 

_run the sample PBT tests_ 

### Mutation Testing

A mutation testing tool will modify conditional logic in the SUT to see if our unit test suite will detect the changes. The modifications are called _mutants_. 

Any mutant that isn't detected by the unit test suite is said to have _survived_. Our goal is to ensure our unit test suite kills all mutants. 

Mutation testing tools only work when the unit test suite is green - that is, all the test cases pass. 

_demonstrate mutation testing_

### Exploratory Testing 

Exploratory Testing is human testing at the level of the entire application. It is not a form of unit checking. 

Typically, a software team will allocate a set amount of time on a regular basis for Exploratory Testing. The whole team participates. 

Someone who is relatively senior in software testing develops a theme for the Exploratory Testing session, and team members work in twos or threes to explore the behavior of the application around that theme. 

Examples of themes include internationalization, accessibilty, usability, user experience, error-handling, or the correctness of a given function of the application, such as transferring funds between bank accounts. 

The combination of different kinds of checking and testing, at different levels of abstraction, helps us gain confidence that our solution will not crash and burn in production. 

But there are no guarantees! Such things as the number of processor cores in a given server, a memory leak in an application that shares a server with ours, gray failures in a cloud environment, and timing issues in distributed applications can't be reliably replicated in a test environment. 

That's the reason we need observability tools in production, and a rational strategy for managing production server instances. Those topics are out of scope here. 








