namespace :cluster do
  task :create do
    sh %Q(
      gcloud container clusters create #{cluster_name} \
        --machine-type #{machine_type} --image-type "COS" \
        --disk-size "10" --num-nodes "#{num_nodes}" \
        --scopes #{cluster_scopes} --network "default" \
        --enable-cloud-logging --enable-cloud-monitoring
        )
  end
  
  task :resize do
    sh %Q(gcloud container clusters resize #{cluster_name} --size=#{num_nodes})
  end
  
  task :delete do
    sh %Q(gcloud container clusters delete #{cluster_name})
  end
end

namespace :helm do
  task :install do
    raise "you must set environment variables DOCKER_IMAGE" unless docker_image 
    sh %Q(gcloud container clusters get-credentials #{cluster_name})
    sh %Q(kubectl version && helm init)
    sh %Q(
      helm install ./charts --namespace locust-gke-test --name locust-gke-test \
        --set image="#{docker_image}" \
        --set slave_count=#{slave_count}
          )
  end
  
  task :delete do
    sh %Q(helm delete locust --purge)
  end
end


def cluster_name
  ENV['CLUSTER_NAME'] || 'locust-gke-test'
end

def machine_type
  ENV['CLUSTER_MACHINE_TYPE'] || 'n1-standard-1'
end

def num_nodes
  ENV['CLUSTER_NUM_NODES'] || 10
end

def docker_image
  ENV['DOCKER_IMAGE']
end

def slave_count
  ENV['SLAVE_COUNT'] || 10
end

def cluster_scopes
  %w(
    "https://www.googleapis.com/auth/compute"
    "https://www.googleapis.com/auth/devstorage.read_only"
    "https://www.googleapis.com/auth/logging.write"
    "https://www.googleapis.com/auth/monitoring"
    "https://www.googleapis.com/auth/servicecontrol"
    "https://www.googleapis.com/auth/service.management.readonly"
    "https://www.googleapis.com/auth/trace.append"
  ).join(",")
end
