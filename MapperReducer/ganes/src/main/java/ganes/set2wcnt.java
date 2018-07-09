package ganes;

import java.io.IOException;
import java.util.*;

import org.apache.hadoop.conf.*;
import org.apache.hadoop.fs.*;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.Mapper.Context;
import org.apache.hadoop.mapreduce.lib.input.*;
import org.apache.hadoop.mapreduce.lib.output.*;
import org.apache.hadoop.util.*;

public class set2wcnt extends Configured implements Tool {

    public static void main(String args[]) throws Exception {
        int res = ToolRunner.run(new set2wcnt(), args);
        System.exit(res);
    }

    public int run(String[] args) throws Exception {
    	
    	if (args.length != 2) {
            System.out.println("usage: [input] [output]");
            System.exit(-1);
        }
    	
        Path inputPath = new Path(args[0]);
        Path outputPath = new Path(args[1]);

        Configuration conf = getConf();
        Job job = new Job(conf, this.getClass().toString());

        FileInputFormat.setInputPaths(job, inputPath);
        FileOutputFormat.setOutputPath(job, outputPath);

        job.setJobName("Optimised Word count");
        job.setJarByClass(wCount.class);
        job.setInputFormatClass(TextInputFormat.class);
        job.setOutputFormatClass(TextOutputFormat.class);

        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(IntWritable.class);

        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        job.setMapperClass(set2map.class);
        //job.setNumReduceTasks(0);
        job.setReducerClass(set2red.class);

        return job.waitForCompletion(true) ? 0 : 1;
    }

    public static class set2map extends Mapper<Object, Text, Text, IntWritable>{
        
        private final IntWritable one = new IntWritable(1);
        
           
        public void map(Object key, Text value, Context context) throws IOException, InterruptedException{
                   
    		String line = value.toString();
    		
    		String text1 = line.replaceAll("[\"#$%^&*@\\-=:;?().,]!''", " ");
            String text2 = text1.toLowerCase();
            
            List<String> set1 = Arrays.asList("fever", "cold", "headache", "stomach", "rash", "vomiting", "dizziness", 
            		"sleepless", "bodypain","bodyache","sorethroat","dysentery","symptom","platelets");
            
            List<String> set2 = Arrays.asList("amoebiasis","typhoid","dengue","malaria","cholera","diseases");
            
                           	
                	//Split each line in text into words by using stringtokenizer
                	
                	StringTokenizer itr = new StringTokenizer(text2);
                		    while (itr.hasMoreTokens()) {
                		    	String temp = itr.nextToken();
                		    	
                		    	if (set2.contains(temp)) {
                		    		context.write(new Text(temp), one);
                		    	}
                		    	
                		    	}
                
                               	
            }

    }
    public static class set2red extends Reducer<Text, IntWritable, Text, IntWritable> {

        
        @Override
        
        public void reduce(Text key, Iterable<IntWritable> values, Context output)
                throws IOException, InterruptedException {
        	int count = 0;
        	    	
            for(IntWritable value: values){
                    	
                count += 1;
            }
            
            output.write(key,new IntWritable(count));
            
                     
            }
    	
    	
    }



}


