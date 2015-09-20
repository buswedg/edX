using System;
using System.Collections.Generic;
using System.Threading;
using System.IO;
using System.Timers;
using System.Runtime.Serialization;
using System.Configuration;
using Microsoft.Hadoop.Avro.Container;
using Microsoft.WindowsAzure.Storage;
using Microsoft.WindowsAzure.Storage.Blob;
using Microsoft.Hadoop.Client;

namespace RaceTracker
{
    #region serialization classes
    // classes for sensor reading objects to be serialized

    [DataContract]
    internal struct Location
    {
        [DataMember]
        public double lat { get; set; }
        [DataMember]
        public double lon { get; set; }
    }

     [DataContract(Name = "GpsReading", Namespace = "CarSensors")]
    internal class GpsReading
    {
        [DataMember(Name = "Time")]
        public string Time { get; set; }

        [DataMember(Name = "Position")]
        public Location Position { get; set; }

        [DataMember(Name = "Speed")]
        public double Speed { get; set; }

    }

    [DataContract(Name = "EngineReading", Namespace = "CarSensors")]
    internal class EngineReading
    {
        [DataMember(Name = "Time")]
        public string Time { get; set; }

        [DataMember(Name = "Revs")]
        public double Revs { get; set; }

        [DataMember(Name="OilTemp")]
        public double OilTemp { get; set; }
    }

    [DataContract(Name = "BrakeReading", Namespace = "CarSensors")]
    internal class BrakeReading
    {
        [DataMember(Name = "Time")]
        public string Time { get; set; }

        [DataMember(Name = "BrakeTemp")]
        public double BrakeTemp { get; set; }

    }

    #endregion


    class Program
    {
        static bool running = false;
        static StreamReader lapData;

        // Lists for captured sensor reading objects
        static List<GpsReading> GpsReadings = new List<GpsReading>();
        static List<EngineReading> EngineReadings = new List<EngineReading>();
        static List<BrakeReading> BrakeReadings = new List<BrakeReading>();

        //files for serialized readings
        static string gpsFile;
        static string engineFile;
        static string brakeFile;

        static void Main(string[] args)
        {
            try
            {
                // race car sensors are simulated in a file, which is read once per second
                string lapFile = new DirectoryInfo(".") + @"\lap.csv";
                lapData = new StreamReader(lapFile);
                System.Timers.Timer lapTimer = new System.Timers.Timer();
                lapTimer.Elapsed += new ElapsedEventHandler(GetReadings);
                lapTimer.Interval = 1000;

                // Drivers, start your engines!
                running = true;
                lapTimer.Start();
                while (running)
                {
                    // vroom, vroom!
                }
                // Chequered flag!
                lapTimer.Stop();
                Console.WriteLine("Lap complete!");

                gpsFile = new DirectoryInfo(".") + @"\gps.avro";
                engineFile = new DirectoryInfo(".") + @"\engine.avro";
                brakeFile = new DirectoryInfo(".") + @"\brake.avro";

                // Serialize the captured data
                SerializeReadings();

                // Upload the serialized data and script files to Azure storage
                UploadFiles();

                // Submit jobs to process the data
                SubmitJobs();


                Console.WriteLine("Press a key to end.");
                Console.Read();
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);

            }
            finally
            {
                Console.WriteLine("Press a key to end.");
                Console.Read();
            }

        }

        private static void GetReadings(object sender, ElapsedEventArgs e)
        {
            string line;
            // check we're not at the end of the file
            if ((line = lapData.ReadLine()) != null)
            {
                // get the individual reading values
                string[] readings = line.Split(',') ;
                string time = DateTime.Now.ToString();

                // Add GPS sensor reading to list for this lap
                Location loc = new Location();
                loc.lat = Double.Parse(readings[0]);
                loc.lon = Double.Parse(readings[1]);
                GpsReading gps = new GpsReading();
                gps.Time = time;
                gps.Position = loc;
                gps.Speed = Double.Parse(readings[4]);
                GpsReadings.Add(gps);

                // Add Engine sensor reading to list for this lap
                EngineReading eng = new EngineReading();
                eng.Time = time;
                eng.Revs = Double.Parse(readings[2]);
                eng.OilTemp = Double.Parse(readings[5]);
                EngineReadings.Add(eng);

                // Add Brake sensor reading to list for this lap
                BrakeReading brake = new BrakeReading();
                brake.Time = time;
                brake.BrakeTemp = Double.Parse(readings[3]);
                BrakeReadings.Add(brake);
                
                // Display readings in the console
                Console.WriteLine(time);
                Console.WriteLine("Position: " + gps.Position.lat.ToString() + "," + gps.Position.lon.ToString());
                Console.WriteLine("Speed: " + gps.Speed.ToString());
                Console.WriteLine("Revs: " + eng.Revs.ToString());
                Console.WriteLine("Oil Temp: " + eng.OilTemp.ToString());
                Console.WriteLine("Brake Temp: " + brake.BrakeTemp.ToString());
                Console.WriteLine("-----------------------------------------------------------");

            }
            else
            {
                running = false;
            }
        }

        static void SerializeReadings()
        {
            try
            {

                //Serialize GPS data to file
                Console.WriteLine("Saving GPS data...");
                using (var buffer = new FileStream(gpsFile, FileMode.Create))
                {
                    //Serialize a sequence of GpsReading objects to stream
                    //Data will be compressed using Deflate codec
                    using (var w = AvroContainer.CreateWriter<GpsReading>(buffer, Codec.Deflate))
                    {
                        using (var writer = new SequentialWriter<GpsReading>(w, 24))
                        {
                            // Serialize the data to stream using the sequential writer
                            GpsReadings.ForEach(writer.Write);
                        }
                    }
                    buffer.Close();
                }

                //Serialize Engine data to file
                Console.WriteLine("Saving engine data...");
                using (var buffer = new FileStream(engineFile, FileMode.Create))
                {
                    //Serialize a sequence of EngineReading objects to stream
                    //Data will be compressed using Deflate codec
                    using (var w = AvroContainer.CreateWriter<EngineReading>(buffer, Codec.Deflate))
                    {
                        using (var writer = new SequentialWriter<EngineReading>(w, 24))
                        {
                            // Serialize the data to stream using the sequential writer
                            EngineReadings.ForEach(writer.Write);
                        }
                    }
                    buffer.Close();
                }

                //Serialize Brake data to file
                Console.WriteLine("Saving brake data...");
                using (var buffer = new FileStream(brakeFile, FileMode.Create))
                {
                    //Serialize a sequence of BrakeReading objects to stream
                    //Data will be compressed using Deflate codec
                    using (var w = AvroContainer.CreateWriter<BrakeReading>(buffer, Codec.Deflate))
                    {
                        using (var writer = new SequentialWriter<BrakeReading>(w, 24))
                        {
                            // Serialize the data to stream using the sequential writer
                            BrakeReadings.ForEach(writer.Write);
                        }
                    }
                    buffer.Close();
                }


            }
            catch (Exception ex)
            {
                Console.WriteLine("An error occurred while serializing the data");
                throw (ex);
            }

        }

        private static void UploadFiles()
        {
            try
            {
                // Get storage configuration settings
                var storageKey = ConfigurationManager.AppSettings["StorageKey"];
                var storageName = ConfigurationManager.AppSettings["StorageName"];
                var storageConnStr = string.Format("DefaultEndpointsProtocol=https;AccountName={0};AccountKey={1}", storageName, storageKey);
                var containerName = ConfigurationManager.AppSettings["ContainerName"];

                CloudStorageAccount storageAccount = CloudStorageAccount.Parse(storageConnStr);
                CloudBlobClient blobClient = storageAccount.CreateCloudBlobClient();
                CloudBlobContainer container = blobClient.GetContainerReference(containerName);

                var destFolder = "data/racecar/source/";

                // Upload GPS data
                Console.WriteLine("Uploading GPS data...");
                CloudBlockBlob gpsBlob = container.GetBlockBlobReference(destFolder + "gps.avro");
                using (var gpsStream = System.IO.File.OpenRead(gpsFile))
                {
                    gpsBlob.UploadFromStream(gpsStream);
                }

                //Upload engine data
                Console.WriteLine("Uploading Engine data...");
                CloudBlockBlob engineBlob = container.GetBlockBlobReference(destFolder + "engine.avro");
                using (var engStream = System.IO.File.OpenRead(engineFile))
                {
                    engineBlob.UploadFromStream(engStream);
                }

                //Upload brake data
                Console.WriteLine("Uploading brake data...");
                CloudBlockBlob brakeBlob = container.GetBlockBlobReference(destFolder + "brake.avro");
                using (var brakeStream = System.IO.File.OpenRead(brakeFile))
                {
                    brakeBlob.UploadFromStream(brakeStream);
                }

                // Upload script files
                destFolder = "data/racecar/scripts/";

                // Upload Pig Script
                Console.WriteLine("Uploading Pig script...");
                var pigFile = new DirectoryInfo(".") + @"\Scripts\ProcessData.pig";
                CloudBlockBlob pigBlob = container.GetBlockBlobReference(destFolder + "processdata.pig");
                using (var pigStream = System.IO.File.OpenRead(pigFile))
                {
                    pigBlob.UploadFromStream(pigStream);
                }

                // Upload Hive Script
                Console.WriteLine("Uploading Hive script...");
                var hiveFile = new DirectoryInfo(".") + @"\Scripts\CreateTables.hql";
                CloudBlockBlob hiveBlob = container.GetBlockBlobReference(destFolder + "createtables.hql");
                using (var hiveStream = System.IO.File.OpenRead(hiveFile))
                {
                    hiveBlob.UploadFromStream(hiveStream);
                }

            }
            catch (Exception ex)
            {
                Console.WriteLine("An error occurred while uploading data files");
                throw (ex);
            }
        }

        private static void SubmitJobs()
        {
            // Get HDInsight cluster configuration settings
            string clusterName = ConfigurationManager.AppSettings["ClusterName"];
            string userName = ConfigurationManager.AppSettings["UserName"];
            string password = ConfigurationManager.AppSettings["Password"];

            // Create basic authentication credential for cluster
            BasicAuthCredential bcred = new BasicAuthCredential();
            bcred.Server = new Uri("https://" + clusterName + ".azurehdinsight.net");
            bcred.UserName = userName;
            bcred.Password = password;

            // Create and submit Pig job
            PigJobCreateParameters pigJob = new PigJobCreateParameters()
            {
                StatusFolder = "/data/racecar/scripts/processdatastatus",
                File = "/data/racecar/scripts/processdata.pig"
            };
            var pigJobClient = JobSubmissionClientFactory.Connect(bcred);
            JobCreationResults pigJobResults = pigJobClient.CreatePigJob(pigJob);
            WaitForJobCompletion(pigJobResults, pigJobClient);

            // Create and submit Hive job
            HiveJobCreateParameters hiveJob = new HiveJobCreateParameters()
            {
                JobName = "Create Hive tables",
                StatusFolder = "/data/racecar/scripts/createtablestatus",
                File = "/data/racecar/scripts/createtables.hql"
            };
            var hiveJobClient = JobSubmissionClientFactory.Connect(bcred);
            JobCreationResults hiveJobResults = hiveJobClient.CreateHiveJob(hiveJob);
            WaitForJobCompletion(hiveJobResults, hiveJobClient);

        }

        private static void WaitForJobCompletion(JobCreationResults jobResults, IJobSubmissionClient client)
        {
            // Wait for job completion, displaying progress
            JobDetails jobInProgress = client.GetJob(jobResults.JobId);
            Console.Write(jobResults.JobId);
            while (jobInProgress.StatusCode != JobStatusCode.Completed && jobInProgress.StatusCode != JobStatusCode.Failed)
            {
                jobInProgress = client.GetJob(jobInProgress.JobId);
                Thread.Sleep(TimeSpan.FromSeconds(5));
                Console.Write(".");
            }
            Console.WriteLine(jobInProgress.StatusCode);
        }

    }
}
