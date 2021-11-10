# Store extra variables that are useful in IIIF Manifests

require "json"

module Jekyll
  class JsonGenerator < Jekyll::Generator
    def generate(site)
        json_files = Array.new;

        site.static_files.delete_if do |sf|
            next if not File.extname(sf.path) == ".json"

            # get the dirname of file, but we don't need the site source
            json_dir = File.dirname(sf.path.gsub(site.source, ""))
            json_name = File.basename(sf.path)

            # add ts file
            json_files << JsonFile.new(site, site.source, json_dir, json_name)
            # return true so this file gets removed from static_files
            # we'll replace it with our own tsfile that implements
            # it's own write
            true
        end

        site.static_files.concat(json_files)
    end
  end
  class JsonFile < Jekyll::StaticFile
        def initialize(site, base, dir, name)
			super(site, base, dir, name, nil)
        end

		def write(dest)
            dest_path = destination(dest)
            return false if File.exist?(dest_path) && !modified?
            if ENV['URL']
                replacements = {
                    "id.url" => ENV['URL'] + @site.config['baseurl'].to_s+ @dir.to_s + "/" + @name.to_s,
                    "id.path" => ENV['URL'] + @site.config['baseurl'].to_s+ @dir.to_s
                }
            else
                replacements = {
                    "id.url" => @site.config['url'].to_s + @site.config['baseurl'].to_s+ @dir.to_s + "/" + @name.to_s,
                    "id.path" => @site.config['url'].to_s + @site.config['baseurl'].to_s+ @dir.to_s
                }

            end
            self.class.mtimes[path] = mtime

            FileUtils.mkdir_p(File.dirname(dest_path))
            FileUtils.rm(dest_path) if File.exist?(dest_path)
            file = File.open path
            begin
                data = JSON.load file
                processHash(data, replacements)
                File.open(dest_path,"w") do |f|
                  f.write(JSON.pretty_generate(data))
                end
            rescue JSON::ParserError => e
                raise 'Failed to load JSON File ' + path + ' due to parse error.'
            end    
		end
        def processHash(hash, replacements)
          hash.each do |key,value|
            if (value.is_a? String) 
                hash[key] = processString(value, replacements)
            end
            if (value.is_a?(Hash)) 
                processHash(value, replacements)
            end
            if (value.is_a?(Array)) 
                processList(value, replacements)
            end
          end
        end  
        def processList(value, replacements) 
            value.each do | object |
                if (object.is_a? String) 
                    processString(object, replacements)
                    # TODO need to add this back into the array somehow
                end
                if (object.is_a?(Hash)) 
                    processHash(object, replacements)
                end
                if (object.is_a?(Array)) 
                    processList(object, replacements)
                end
            end
        end
        def processString(value, replacements)
          if (value.include? "{{")
                replacements.each do |replacement_key, replacement_value|
                    if value.match(/{{[ ].*#{replacement_key}[ ].*}}/)
                        return value.gsub(/{{[ ].*#{replacement_key}[ ].*}}/,replacement_value)
                    end
                end    
            end
            return value
        end
	end
end
