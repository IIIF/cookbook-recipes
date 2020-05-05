---
title: IIIF Cookbook Process
layout: recipe
---

The cookbook-recipes repository is a Jekyll website, like the main IIIF site, with [some additions](https://github.com/IIIF/cookbook-recipes/#jekyll-variables) to make it easier to manage recipes and their dependent parts. In the IIIF specifications site, JSON-LD examples are embedded snippets in the page markdown. But in the recipes repository, code must be complete and standalone - we need our recipes to be complete working examples, not just extracts for guidance. Typically a recipe will include an entire manifest, as a separate JSON-LD file, that points to real assets, that works in a viewer. 

Recipes start with an issue in the [Cookbook Repository](https://github.com/IIIF/cookbook-recipes/issues) and anyone can submit a recipe to the cookbook. Sometimes the person who raises the recipe issue then goes on to write the recipe, but this doesn't have to be the case. The need for a recipe may be expressed before its form is known; the comments on the recipe issue are where the recipe is discussed and elaborated.

Recipes should not be substantially the same as an existing recipe (though may demonstrate an extension of an existing recipe, and therefore reproduce it).

Each issue has a corresponding directory in the Cookbook repository (the recipe issue number is the directory name). Under this directory, index.md is the home page of the issue. The recipe should be accompanied by complete JSON-LD files, with working links to content and other resources. Large binary resources such as videos can be uploaded to the shared recipe fixtures S3 bucket. Where a working Image Service is required, the reference image server may be used and details of this service can be found in the discussion of fixtures below.

A recipe must have the following features:

* A short and clear name.
* A use case (why the pattern is important to include).
* Implementation notes, with references to the specification and other recipes;
* All referenced content resources, external annotations and other links should resolve: they must exist on the web and resolve. 
    * Any client that implements support for a recipe should expect the published recipe to work. 
    * As much as possible the content resources should be hosted on the fixtures.iiif.io web site, rather than at third party locations. 
* Restrictions (optional): where this pattern is usable or not usable, with explanation of why
* A full example, comprising:
    * a prose description;
    * code samples (JSON-LD representation, following the formatting instructions below)
* See also: similar or otherwise related recipes. This recipe may build on other recipes, or may be a building block in subsequent recipes.
* Finally recipes must be linked to from the `index.md` page and be present in the `links.md` file. 

**Note**: all recipes should show IIIF version 3.0 features.

For a completed example see:

[Simplest Manifest - Single Image File](https://github.com/IIIF/cookbook-recipes/tree/master/recipe/0001-mvm-image)

Once you have created a recipe and created a pull request. This will be evaluated by the Cookbook community, Cookbook editors and the [Technical Review Committee](https://iiif.io/community/trc/). Comments will be fed back to the author at all stages and once the Technical Review Committee has approved it, the pull request will be merged to the master branch. 

# Full process

* The proposer creates an issue for the recipe on GitHub.
* The initial discussion of the recipe is conducted in comments on the issue and through the Cookbook channel on the [IIIF Slack](http://bit.ly/iiif-slack). This may result in the recipe being modified, or abandoned.
* If there is broad agreement that the recipe is valuable, the proposer, or another community member assigns the issue to themselves. 
  * To get permission to assign issues please contact the IIIF Staff at admin@iiif.io who will add you to the _iiif-recipes_ Github team. 
* Clone the cookbook repository
* Create a new branch locally to work on your recipe
* Push this branch to the [IIIF/Cookbook](https://github.com/IIIF/cookbook-recipes) repository 
  * This will ensure later deployment preview functionality will run
* The assignee will then create a draft pull request with this new branch
* Once the assignee has completed their work on the pull request they move the pull request out of draft by clicking 'Ready for Review'
* Review process
  * Informal review by Cookbook group (announce on Cookbook slack channel)
    * Pull requests out of draft
  * First review by Cookbook Editors group
    * Pull request marked with _ready-for-editors_
  * Final approval by the Technical Review Committee and after this the pull request will be merged to master)
    * Pull requests marked with _ready-for-trc_
  * If approved pull request is merged with the master  

Note if there are a large amount of changes requested, the pull requests maybe sent back to community review state

# Fixtures

While all JSON-LD (Manifests, Collections, Annotation pages, etc) should be part of the recipe pull request on GitHub, any binary assets such as images, audio and video should be uploaded to the fixtures Amazon S3 bucket. Please contact Glen Robson, IIIF Technical Coordinator to get login credentials to be able to add assets to this s3 bucket. 

The fixtures site provides a front end to view the fixture that are in the fixtures s3 bucket. Image assets in the fixtures site have a IIIF Image API endpoint available for use in your recipe.

[https://fixtures.iiif.io/](https://fixtures.iiif.io/) 

The first page allows you to navigate the assets by format; image, audio and video. Once you have found an asset click on the file to be taken to a page showing information on this asset including duration, spatial dimensions and in the case of images a IIIF Image API endpoint. 

{% include acronyms.md %}
{% include links.md %}
