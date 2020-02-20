require 'open3'
require 'fileutils'
require 'base64'

# Base location of where to store JPGs extracted from MPEGs.
$evidence_dir = '/Users/stephenstewart/Documents/Working/Testing'

def nuix_worker_item_callback(item)
	source_item = item.source_item
	source_item_guid = item.item_guid
	source_item_type = source_item.type.name
	source_item_name = source_item.name
	source_item_properties = source_item.properties

	if source_item_type == 'application/vnd.kafka.message'
		puts "NAME: #{source_item_name}"
		puts "PROP.COUNT: #{source_item_properties.size}"

		# Create the evidence directory for this item based off its GUID to store the items in.
		output_dir = "%s/%s/%s" % [$evidence_dir, source_item_guid[0,3], source_item_guid[3,3]]
		FileUtils.mkdir_p(output_dir)
		child_items = Array.new
		# Scan the JSON properties of the Kakfa message looking for the field that contains the HTML - "content"
		source_item_properties.each do |key,value|
			if key == 'content'
				#Extract the "content" value, decode it, and write it out to a file.
				#There is no file extension.  The Nuix engine will sort it out.
				outputFile = File.new("#{output_dir}/#{source_item_guid}",'w')
				outputFile.write(Base64.decode64(value))
				outputFile.close
				#Add the path to an array that will then be added to the item.
				child_items.push("#{output_dir}/#{source_item_guid}")
			end
		end
		item.children = child_items
	end
end