spec = Gem::Specification.find_by_name 'iiifc-theme'
Dir.glob("#{spec.gem_dir}/lib/tasks/*.rake").each { |r| load r }

# configure default task
task ci: 'cookbook:ci'
task default: :ci

namespace :cookbook do
  desc 'run cookbook tests'
  desc 'Build CI site, run html-proofer and spec tests'
  task :ci do
    Rake::Task['build:ci'].invoke
    Rake::Task['test:html'].invoke
    Rake::Task['test:links:internal'].invoke
    Rake::Task['test:links:iiif'].invoke
  end
end  
